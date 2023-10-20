import logging
import logging.handlers
import toml
import os

# Define the path to the settings.toml file
SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.toml")

try:
    settings = toml.load(SETTINGS_FILE)
    logMaxMb = settings.get("logSizeMb", 10)
except FileNotFoundError:
    logMaxMb = settings['logs']['logSizeMb']


print(settings['logs']['logSizeMb'])


FILE_PATH = (os.path.dirname(__file__) + "/")
print("file path >", FILE_PATH)
# Own logger object
Logger = logging.getLogger('main')

# Own handler object
loggerPath = FILE_PATH + 'logs/'
Handler = logging.handlers.RotatingFileHandler(filename=os.path.join(loggerPath, "Test.log"),
                                              mode='a',
                                              maxBytes=logMaxMb * 1024 * 1024,
                                              backupCount=1,
                                              encoding=None,
                                              delay=False,
                                              )

# Own formatter object
formatter = logging.Formatter(
    "%(asctime)s::%(levelname)s::%(filename)s::%(lineno)d %(message)s"
)

# Link logger, handler, and formatter
Logger.setLevel(logging.DEBUG)
Handler.setFormatter(formatter)
Logger.addHandler(Handler)
Logger.debug("logger is set")

