import logging.config

from work_08_01_main import print_primes
from primes_package.work_08_01_log_settings import log_config

logging.config.dictConfig(log_config)

print_primes(30)