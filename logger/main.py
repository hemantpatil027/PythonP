"""this main is to check logging to same log file from different py files
continuously, main_func and dummy_func will write data in test.log file
both functions are called in thread.
to see if it could crash the operation
"""
from logger import Logger as logger
import time
import threading

from sub_main import *

logger.debug("logger object is used in main")

def main_func():
    try:
        while True:
            time.sleep(0.001)
            logger.debug("Test Log from main_func called in thread.")
    except Exception as e:
        logger.exceptoin(f"exception in main_func in main: {str(e)}")

if __name__ == "__main__":
    try:
        main_func_thread = threading.Thread(target=main_func)
        main_func_thread.start()

        dummy_func_thread = threading.Thread(target=dummy_func)
        dummy_func_thread.start()

    except Exception as e:
        logger.exception(f"exception in main: {str(e)}")
