import signal
import sys
from server import app, start_scheduler, stop_scheduler, cache_fuels


def handle_shutdown(signum, frame):
    stop_scheduler()
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)

cache_fuels()
start_scheduler()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
