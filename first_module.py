import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
FORMAT = "%(asctime)-15s [%(filename)s:%(lineno)d] :%(levelname)8s: %(message)s: %(name)s"

formatter = logging.Formatter(FORMAT)

file_handler = logging.FileHandler('first_module_handler.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("logging debug first module")
logger.info("logging info first module")

print("name = {}".format(__name__))