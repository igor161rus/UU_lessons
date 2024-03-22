log_config = {
    'version': 1,
    'formatters': {
        'info_formatter': {
            'format': '%(levelname)s - %(asctime)s - %(message)s'
        },
        'warning_formatter': {
            'format': '%(levelname)s - %(message)s'
        },
        'debug_formatter': {
            'format': '%(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'info_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'info_formatter',
            'filename': 'info.log',
            'encoding': 'utf-8',
        },
        'warning_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'warning_formatter',
            'filename': 'warning.log',
            'encoding': 'utf-8',
        },
        'debug_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'debug_formatter',
            'filename': 'debug.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'info': {
            'handlers': ['info_handler'],
            'level': 'INFO'
        },
        'warning': {
            'handlers': ['warning_handler'],
            'level': 'WARNING'
        },
        'debug': {
            'handlers': ['debug_handler'],
            'level': 'ERROR'
        },
    },
}

