log_config = {
    'version': 1,
    'formatters': {
        'success_formatter': {
            'format': '%(asctime)s - %(message)s'
        },
        'bad_formatter': {
            'format': '%(asctime)s - %(message)s'
        },
        'blocked_formatter': {
            'format': '%(asctime)s - %(message)s'
        },
    },
    'handlers': {
        'success_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'success_formatter',
            'filename': 'success_responses.log',
            'encoding': 'utf-8',
        },
        'bad_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'bad_formatter',
            'filename': 'bad_responses.log',
            'encoding': 'utf-8',
        },
        'blocked_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'blocked_formatter',
            'filename': 'blocked_responses.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'success': {
            'handlers': ['success_handler'],
            'level': 'INFO'
        },
        'bad': {
            'handlers': ['bad_handler'],
            'level': 'INFO'
        },
        'blocked': {
            'handlers': ['blocked_handler'],
            'level': 'INFO'
        },
    },
}

