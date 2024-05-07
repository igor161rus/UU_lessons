import logging.config
from log_settings import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger('Logger')

log_w = logging.getLogger('warning')
log_i = logging.getLogger('info')
