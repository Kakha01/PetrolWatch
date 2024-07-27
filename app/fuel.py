import requests
import utils
from bs4 import BeautifulSoup, NavigableString
from typing import TypedDict
import sqlite3
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Encoding": "utf-8",
}

Fuel = TypedDict(
    "Fuel",
    {
        "company_name": str,
        "name": str,
        "price": str,
        "type": str,
    },
)

s = requests.Session()
s.headers.update(HEADERS)


def fetch_html(url: str):
    try:
        response = s.get(url, verify=False)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    except Exception as e:
        print(e)


def fetch_json(url: str):
    try:
        response = s.get(url, verify=False)
        return response.json()
    except Exception as e:
        print(e)


def add_fuels_to_db(db: sqlite3.Connection, fuel_info: list[Fuel]):
    cur = db.cursor()
    for fuel in fuel_info:
        try:
            cur.execute(
                "INSERT INTO fuel (company_name, fuel_name, fuel_price, fuel_type) VALUES (?, ?, ?, ?)",
                (fuel["company_name"], fuel["name"], fuel["price"], fuel["type"]),
            )
        except sqlite3.IntegrityError:
            print("Database Integrity Error")

    db.commit()
    cur.close()


def get_socar_fuels() -> list[Fuel] | None:
    soup = fetch_html("https://www.sgp.ge/en/")
    if not soup:
        return None

    return extract_socar_fuel_info(soup)


def extract_socar_fuel_info(soup: BeautifulSoup):
    # Target:
    # <li data-percent="74.4">
    #   <span>Nano Super</span>
    #   <div class="progress">
    #     <div class="progress-percent">
    #       <div class="counter counter-inherit counter-instant">3.72 ₾</div>
    #     </div>
    #   </div>
    # </li>

    fuels: list[Fuel] = []

    for li in soup.find_all("li", attrs={"data-percent": True}):
        fuel_name = li.span.text
        fuel_price = li.div.div.div.text.split("  ")[0].strip()
        fuel_type = utils.sluggify_fuel(fuel_name)
        if fuel_type:
            fuels.append(
                {
                    "company_name": "Socar",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels


def get_lukoil_fuels() -> list[Fuel] | None:
    soup = fetch_html("http://lukoil.ge")
    if not soup:
        return None

    return extract_lukoil_fuel_info(soup)


def extract_lukoil_fuel_info(soup: BeautifulSoup):
    # Target:
    # <table class="table table-orange table-striped">
    #   <tbody>
    #     <tr>
    #       <td>efix Super</td>
    #       <td>3.77</td>
    #     </tr>
    #   </tbody>
    # </table>

    fuels: list[Fuel] = []

    for div in soup.find_all(
        "div",
        attrs={
            "class": "mt-4 w-full h-2/5 flex justify-center items-center text-xl text-lk-main flex-col"
        },
    ):
        fuel = div.find_all("p")
        fuel_name = fuel[1].text.strip()
        fuel_price = fuel[0].text.strip()
        fuel_type = utils.sluggify_fuel(fuel_name)

        if fuel_type:
            fuels.append(
                {
                    "company_name": "Lukoil",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels


def get_rompetrol_fuels() -> list[Fuel] | None:
    soup = fetch_html("https://www.rompetrol.ge/en/")
    if not soup:
        return None

    return extract_rompetrol_fuel_info(soup)


def extract_rompetrol_fuel_info(soup: BeautifulSoup):
    # Target:
    # <table class="table table-orange table-striped">
    #   <tbody>
    #     <tr>
    #       <td>efix Super</td>
    #       <td>3.77</td>
    #     </tr>
    #   </tbody>
    # </table>

    fuels: list[Fuel] = []

    table = soup.find("table", attrs={"class": "table table-orange table-striped"})

    if not isinstance(table, NavigableString) and table is not None:
        for tr in table.find_all("tr"):
            fuel = tr.find_all("td")
            if len(fuel) < 1:
                continue

            fuel_name = fuel[0].text.strip()
            fuel_price = fuel[1].text.strip()
            fuel_type = utils.sluggify_fuel(fuel_name)

            if fuel_type:
                fuels.append(
                    {
                        "company_name": "Rompetrol",
                        "name": fuel_name,
                        "price": fuel_price,
                        "type": fuel_type,
                    }
                )

    return fuels


def get_gulf_fuels() -> list[Fuel] | None:
    soup = fetch_html("https://gulf.ge/en/")
    if not soup:
        return None
    return extract_gulf_fuel_info(soup)


def extract_gulf_fuel_info(soup: BeautifulSoup):
    # Target:
    # <div class="price_entry">
    #   <div class="product_name">G-Force Super</div>
    #   <div class="product_price">3.77</div>
    # </div>

    fuels: list[Fuel] = []

    for div in soup.find_all("div", attrs={"class": "price_entry"}):
        fuel = div.find_all("div")
        fuel_name = fuel[0].text.strip()
        fuel_price = fuel[1].text.strip()
        fuel_type = utils.sluggify_fuel(fuel_name)

        if fuel_type:
            fuels.append(
                {
                    "company_name": "Gulf",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels


def get_optima_fuels() -> list[Fuel] | None:
    soup = fetch_html("http://optimapetrol.ge/en")
    if not soup:
        return None
    return extract_optima_fuel_info(soup)


def extract_optima_fuel_info(soup: BeautifulSoup):
    # Target:
    # <div class="col-xl-3 col-md-6 col-12">
    #   <div
    #     class="product d-flex align-items-center bg-success justify-content-between"
    #   >
    #     <h2 class="key text-white">Premium</h2>
    #     <div class="val text-white">3.30</div>
    #   </div>
    # </div>

    fuels: list[Fuel] = []

    for div in soup.find_all("div", attrs={"class": "col-xl-3 col-md-6 col-12"}):
        fuel_name = div.div.h2.text.strip()
        fuel_price = div.div.div.text.strip()
        fuel_type = utils.sluggify_fuel(fuel_name)

        if fuel_type:
            fuels.append(
                {
                    "company_name": "Optima",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels


def get_portal_fuels() -> list[Fuel] | None:
    soup = fetch_html("https://portal.com.ge/english/home")
    if not soup:
        return None
    return extract_portal_fuel_info(soup)


def extract_portal_fuel_info(soup: BeautifulSoup):
    # Target:
    # <div class="fuel_table">
    #   <table>
    #     <tr>
    #       <td>
    #         <div class="fuel_title">
    #           EFFECT DIESEL
    #           <div class="color_title2">+</div>
    #         </div>
    #       </td>
    #       <td>
    #         <div class="fuel_price">
    #           <div class="old_fuel_price_wrapper">
    #             <p class="old_fuel_price">3.30</p>
    #           </div>
    #         </div>
    #       </td>
    #     </tr>
    #   </table>
    # </div>

    fuels: list[Fuel] = []

    for div in soup.find_all("div", attrs={"class": "fuel_table"}):
        fuel = div.table.tr.find_all("td")
        fuel_name = fuel[0].div.text.strip().strip("\t93+")
        fuel_price = fuel[1].div.div.p.text.strip()
        fuel_type = utils.sluggify_fuel(fuel_name)

        if fuel_type:
            fuels.append(
                {
                    "company_name": "Portal",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels


def get_wissol_fuels() -> list[Fuel] | None:
    json = fetch_json(
        "https://wissol.ge/adminarea/api/ajaxapi/get_fuel_prices?lang=eng"
    )
    if not json:
        return None
    return extract_wissol_fuel_info(json)


def extract_wissol_fuel_info(json: list[dict[str, str]]):
    # Target:
    # [
    #   {
    #     "fuel_name": "EKO SUPER",
    #     "fuel_price": "3.75",
    #   },
    # ]

    fuels: list[Fuel] = []

    for fuel in json:
        fuel_name = fuel["fuel_name"]
        fuel_price = fuel["fuel_price"]
        fuel_type = utils.sluggify_fuel(fuel_name)

        if fuel_type:
            fuels.append(
                {
                    "company_name": "Wissol",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels


def get_connect_fuels() -> list[Fuel] | None:
    json = fetch_json("https://connect-database.vercel.app/api/data")
    if not json:
        return None
    return extract_connect_fuel_info(json)


def extract_connect_fuel_info(json: list[dict[str, str]]):
    # Target:
    # [
    #   {
    #     "_id": "65686b2f505b0981400de648",
    #     "id": 1,
    #     "price": "2.84",
    #     "nameGe": "რეგულარი",
    #     "nameEn": "Regular",
    #     "__v": 0
    #   },
    # ]

    fuels: list[Fuel] = []

    for fuel in json:
        fuel_name = fuel["nameEn"]
        fuel_price = fuel["price"]
        fuel_type = utils.sluggify_fuel(fuel_name)

        if fuel_type:
            fuels.append(
                {
                    "company_name": "Connect",
                    "name": fuel_name,
                    "price": fuel_price,
                    "type": fuel_type,
                }
            )

    return fuels
