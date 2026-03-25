import time
import logging
from flask_http_middleware import BaseHTTPMiddleware
from logging.handlers import TimedRotatingFileHandler
import os, dotenv

# Ensure the logs directory exists
os.makedirs(os.getenv('LOGS_LOCATION'), exist_ok=True)

# Set up the log handler
handler = TimedRotatingFileHandler(
    filename=os.getenv('LOGS_LOCATION') + '/Caab.log',
    when='midnight',
    encoding='utf-8'
)

formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
handler.setFormatter(formatter)

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Optional: disable default Flask logger duplication
logger.propagate = False

# Middleware
class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self):
        super().__init__()

    def dispatch(self, request, call_next):
        start_time = time.time()
        method = request.method
        path = request.path
        ip = request.remote_addr

        response = call_next(request)

        duration = round(time.time() - start_time, 4)
        status = response.status_code

        logger.info(f"{ip} {method} {path} → {status} [{duration}s]")

        return response