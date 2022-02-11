
import logging
import logging.config

# Loading logging config from logging.conf file
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

try:
    'a' + 2
    logger.info('Sum succesfully done')
except TypeError:
    logger.info("Can't sum", exc_info=True)


logger.info('Informacion')

