import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%m/%d/%Y %H:%M:%S')

import helper

log.debug("Debug message")
log.info("Info message")
log.warning("Warning message")
log.error("Error message")
log.critical("Critical message")
