import logging
import sys
logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s", filename="student.log")
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
FORMAT = "%(name)s: %(message)s"
formatter = logging.Formatter(FORMAT)
file_handler = logging.FileHandler('student_handler.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout) #we now have a stream handler also
stream_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stream_handler) # also adding the stream handler


class student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("created stduent - first name = {}, second name = {}".format(self.first, self.last))

student_1 = student("pyari", "singh")
student_2 = student("madhav", "sai")
student_3 = student("premith", "kannathan") 