import logging

import urllib3
from apscheduler.schedulers.background import BackgroundScheduler
from cache import cache_fuels, get_fuels
from flask import Flask, render_template
from pytz import utc

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

scheduler = BackgroundScheduler(timezone=utc)
scheduler.add_job(func=cache_fuels, trigger="interval", hours=1)


@app.route("/")
def index():
    return render_template("index.html", fuels=get_fuels())


def start_scheduler():
    try:
        scheduler.start()
        logger.info("Scheduler started successfully")
    except Exception as e:
        logger.error(f"Error starting scheduler: {e}")


def stop_scheduler():
    scheduler.shutdown()
    logger.info("Scheduler shut down")
