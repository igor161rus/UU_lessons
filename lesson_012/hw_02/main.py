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
    except requests.exceptions.RequestsWarning:
        # elif response.status_code == 403 or response.status_code == 503:
            log = logging.getLogger('bad')
            log.warning(f'{site}, response - {response.status_code}')
    except requests.exceptions.ReadTimeout:
        log = logging.getLogger('blocked')
        log.error(f'{site}, response - NO CONNECTION')
    # except requests.exceptions.ConnectTimeout:
    #     print('Oops. Connection timeout occured!')
    # except Exception:
    #     log = logging.getLogger('blocked')
    #     log.error(f'{site}, response - NO CONNECTION')
