from logger import Logger as logger
import time
logger.debug("logger object is used in sub_main")


def dummy_func():
    try:
        while True:
            time.sleep(0.001)
            logger.debug("Test Log from sub_main called in thread.")
    except Exception as e:
        logger.exceptoin(f"exception in dummy_func in sub_main: {str(e)}")