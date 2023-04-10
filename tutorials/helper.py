import logging

logger = logging.getLogger(__name__)
# logger.propagate = False

# create a log handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and the format
stream_h.setLevel(logging.INFO)
file_h.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.info("Info message")
logger.warning("Warning message")
