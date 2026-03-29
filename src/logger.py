import logging
import os
from datetime import datetime

# Create logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Create log file with timestamp
log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_filepath = os.path.join(logs_dir, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)