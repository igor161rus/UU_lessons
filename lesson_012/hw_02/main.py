import requests
import requests as rq
import logging
import logging.config
from log_settings import log_config

logging.config.dictConfig(log_config)

logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            log = logging.getLogger('success')
            log.info(f'{site}, response - {response.status_code}')
        elif response.status_code == 403 or response.status_code == 503:
            log = logging.getLogger('bad')
            log.warning(f'{site}, response - {response.status_code}')
    except requests.exceptions.ReadTimeout:
        log = logging.getLogger('blocked')
        log.error(f'{site}, response - NO CONNECTION')

# Результат:
# success_responses.log:
# INFO - https://www.youtube.com/, response - 200
# INFO - https://wikipedia.org, response - 200
# INFO - https://yahoo.com, response - 200
# INFO - https://yandex.ru, response - 200
# INFO - https://whatsapp.com, response - 200
# INFO - https://tiktok.com, response - 200
#
# bad_responses.log:
# WARNING - https://amazon.com, response - 503
# WARNING - https://www.ozon.ru, response - 403
#
# blocked_responses.log:
# ERROR - https://instagram.com, response - NO CONNECTION
# ERROR - https://twitter.com, response - NO CONNECTION
