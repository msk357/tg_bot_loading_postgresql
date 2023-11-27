"""
Модуль для настройки логгирования.
Используется стандартная библиотека logging.
"""
import logging


log_format = f'%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)s'


def logger_get(name):
    logger_name = logging.getLogger(name)
    return logger_name


file_handler = logging.FileHandler('logs_tg_bot.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))
logger = logger_get(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
