import logging
import allure
import yaml
import time
from requests import Response
from functools import wraps

# Load configuration from config.yaml
with open("config.yaml", "r") as f:
    config =yaml.safe_load(f)

log_level = config.get("logging", {}).get("level", "INFO").upper()
log_file = config.get("logging", {}).get("file", "api_test_logs.log")

# Configure a logger
logger = logging.getLogger("api-logger")
logger.setLevel(getattr(logging, log_level, logging.INFO))

# Add a file handler for logs
file_handler = logging.FileHandler("api_test_logs.log", mode="w")
file_handler.setLevel(getattr(logging, log_level, logging.INFO))

# Add a console handler for debug-level logs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Set a common format for logs
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_api_calls(func):
    """
    A decorator to log API requests and responses automatically
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # Call to the original method
        response = func(*args, **kwargs)
        end_time = time.time()

        # Extract request and response details
        if isinstance(response, Response):
            duration = end_time - start_time
            logger.info(f"API call took {duration: .2f} seconds")
            # Handle request body safely
            request_body = response.request.body
            if request_body and isinstance(request_body, (bytes, bytearray)):
                request_body = request_body.decode("utf-8", errors="ignore")
                
            # Request details
            request_log = (
                f"Request:\n"
                f"Method: {response.request.method}\n"
                f"URL: {response.request.url}\n"
                f"Headers: {response.request.headers}\n"
                f"Payload: {response.request.body}\n"
            )
            logger.info(request_log)

            # Response details
            response_log = (
                f"Response:\n"
                f"Status Code: {response.status_code}\n"
                f"Headers: {response.headers}\n"
                f"Body: {response.text}\n"
            )
            logger.info(response_log)

            # Attach logs to Allur report
            with allure.step(f"Request: {response.request.method} {response.request.url}"):
                allure.attach(f"Duration: {duration: .2f} seconds", name="Call Duration", attachment_type=allure.attachment_type.TEXT)
                allure.attach(request_log, name="Request Details", attachment_type=allure.attachment_type.TEXT)
                allure.attach(response_log, name="Response Details", attachment_type=allure.attachment_type.TEXT)
        return response
    return wrapper