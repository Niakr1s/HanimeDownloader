import logging

# create logger with 'spam_application'
logger = logging.getLogger("hanime_downloader")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler("hanime_downloader.log")
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def info(event: str, details: str):
    logger.info(f"{event}: {details}")


def error(event: str, details: str):
    logger.error(f"{event}: {details}")
