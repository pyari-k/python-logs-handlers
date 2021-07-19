#import first_module
import logging 
logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)d] :%(levelname)8s: %(message)s: %(name)s"

logging.basicConfig(level=logging.DEBUG,format=FORMAT,filename="second_module_handler.log")


logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
file_handler = logging.FileHandler('first_module_handler.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("logging debug second module")
logger.info("logging info second module")