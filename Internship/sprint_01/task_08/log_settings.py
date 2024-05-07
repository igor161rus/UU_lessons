log_config = {
    'version': 1,
    'formatters': {
        'info_formatter': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
        'debug_formatter': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
        'warning_formatter': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'info_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'info_formatter',
            'filename': 'log/info.log',
            'encoding': 'utf-8',
        },
        'debug_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'debug_formatter',
            'filename': 'log/debug.log',
            'encoding': 'utf-8',
        },
        'warning_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'warning_formatter',
            'filename': 'log/warning.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'info': {
            'handlers': ['info_handler'],
            'level': 'INFO'
        },
        'debug': {
            'handlers': ['debug_handler'],
            'level': 'DEBUG'
        },
        'warning': {
            'handlers': ['warning_handler'],
            'level': 'WARNING'
        },
    },
}
