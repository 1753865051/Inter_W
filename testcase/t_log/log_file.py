import logging


logger = logging.getLogger("log_file_demo")
logger.setLevel(logging.INFO)
fh_steam=logging.StreamHandler()
fh_steam.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
fh_steam.setFormatter(formatter)
logger.addHandler(fh_steam)
logger.info('info')
logger.debug('debug')
logger.warning('warning')