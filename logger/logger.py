import logging
import logging.handlers
import toml
import os
FILE_PATH = (os.path.dirname(__file__) + "/")
print("file path >",FILE_PATH)

logMaxMb = 10

#own logger object
Logger = logging.getLogger('main')

# own handler object
loggerPath=FILE_PATH + 'logs/'
# Handler = logging.FileHandler(filename=loggerPath + "Beltlog.log",)
Handler = logging.handlers.RotatingFileHandler(filename= loggerPath + "Test.log", 
                                      mode='a', 
                                      maxBytes=logMaxMb*1024*1024, 
                                      backupCount=1, 
                                      encoding=None, 
                                      delay=False, 
                                      
                                     )

# own formater object
formatter = logging.Formatter(
    "%(asctime)s::%(levelname)s::%(filename)s::%(lineno)d %(message)s"
)

# link logger,handler and formater
Logger.setLevel(logging.DEBUG)
Handler.setFormatter(formatter)
Logger.addHandler(Handler)
Logger.debug("logger is set")


