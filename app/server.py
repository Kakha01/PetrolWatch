import fuel
from apscheduler.schedulers.background import BackgroundScheduler
from cache import cache
from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

# Recaches every 12 hours
scheduler = BackgroundScheduler()
scheduler.add_job(func=fuel.cache_fuels, trigger="interval", hours=12)
scheduler.start()


@app.route("/")
def index():
    return render_template("index.html", fuels=cache)


if __name__ == "__main__":
    try:
        fuel.cache_fuels()
        serve(app, host="0.0.0.0", port="8080")
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
