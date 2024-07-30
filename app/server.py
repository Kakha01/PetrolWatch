import logging

import fuel
import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
from cache import fuels_cache_categorised
from flask import Flask, render_template
from waitress import serve

logging.basicConfig(level=logging.INFO)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


app = Flask(__name__)

# Recaches every 12 hours
scheduler = BackgroundScheduler()
scheduler.add_job(func=fuel.cache_fuels, trigger="interval", hours=1)
scheduler.start()


@app.route("/")
def index():
    return render_template("index.html", fuels=fuels_cache_categorised)


if __name__ == "__main__":
    try:
        fuel.cache_fuels()
        serve(app, host="0.0.0.0", port="8080")
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
