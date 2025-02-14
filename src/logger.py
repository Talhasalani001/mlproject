import logging  # Correct module name
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")  # Create logs directory
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Correct path join

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Fix comma issue
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,  # Fix comma issue
)  

