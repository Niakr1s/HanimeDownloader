import logging

logger = logging.getLogger("hanime_downloader")
logger.setLevel(logging.DEBUG)
logger.propagate = False

fh = logging.FileHandler("hanime_downloader.log")
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


def info(event: str, details: str):
    logger.info(f"{event}: {details}")


def error(event: str, details: str):
    logger.error(f"{event}: {details}")
