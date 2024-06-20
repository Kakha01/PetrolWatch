import requests
import utils
from bs4 import BeautifulSoup
from typing import TypedDict
from db import connect_db
import sqlite3

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

Fuel = TypedDict(
    "Fuel",
    {
        "id": int,
        "company_name": str,
        "fuel_name": str,
        "fuel_price": str,
        "fuel_type": str,
    },
)


def get_fuels() -> list[Fuel]:
    raise NotImplementedError()


def get_socar_fuels():
    db = connect_db()
    response = requests.get(
        "https://www.sgp.ge/en/",
        headers={"User-Agent": USER_AGENT, "Encoding": "utf-8"},
    )

    content = response.content

    soup = BeautifulSoup(content, "html.parser")

    company_name = "Socar"

    cur = db.cursor()

    for li in soup.find_all("li", attrs={"data-percent": True}):
        fuel_name: str = li.span.text
        fuel_price: str = (
            li.find("div", attrs={"class": "counter counter-inherit counter-instant"})
            .text.split("  ")[0]
            .strip()
        )
        fuel_type = utils.sluggify_fuel(fuel_name)

        if not fuel_type:
            continue

        try:
            cur.execute(
                "INSERT INTO fuel (company_name, fuel_name, fuel_price, fuel_type) VALUES (?, ?, ?, ?)",
                (company_name, fuel_name, fuel_price, fuel_type),
            )
        except sqlite3.IntegrityError:
            print("Fuel already exists")
            continue

    db.commit()
    cur.close()

    cur = db.cursor()

    return cur.execute("SELECT * FROM fuel").fetchall()


if __name__ == "__main__":
    get_socar_fuels()
