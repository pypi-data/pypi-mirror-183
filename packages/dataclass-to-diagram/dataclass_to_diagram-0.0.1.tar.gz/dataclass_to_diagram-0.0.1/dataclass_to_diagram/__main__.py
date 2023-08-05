import logging
import sys

from .main.main import generate_images

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

# if __name__ == "__main__":
#     log.info("Script for generating images started")
#     print(sys.argv)


def start():
    log.info("Script for generating images started")
    print(sys.argv)
