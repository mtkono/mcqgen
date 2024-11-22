import logging
import os
from datetime import datetime

LOGS_FOLDER_PATH=os.path.join(os.getcwd(),"logs")
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH=os.path.join(LOGS_FOLDER_PATH,LOG_FILE)

os.makedirs(LOGS_FOLDER_PATH,exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")
