import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #cwd=current working directory
os.makedirs(logs_path,exist_ok=True) # Create 'logs' directory if it doesn't exist if already exist append it

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

"""
Purpose:
This setup creates unique log files with timestamps in their names, organized in a logs directory, making it easy to:

Track when each log was created

Prevent overwriting old logs

Keep logs organized by creation time
"""


