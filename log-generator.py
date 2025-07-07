import time
import logging

logging.basicConfig(filename="/var/log/test-app.log", level=logging.INFO)

while True:
    logging.info("Hello from test app log")
    time.sleep(5)

