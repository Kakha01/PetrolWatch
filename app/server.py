from flask import Flask, render_template
from waitress import serve
import os
from db import init_db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["DATABASE"] = os.path.join(basedir, "cache.db")

with app.app_context():
    init_db()


@app.route("/")
def index():
    return render_template("index.html", heading_text="Hello World!")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port="8080")
