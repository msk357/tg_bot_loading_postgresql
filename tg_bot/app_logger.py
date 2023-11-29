"""
Модуль для настройки логгирования. Используется стандартная библиотека logging.
Настроено обновление логов по размеру файла, атрибут maxBytes.
Лог-файлы сохраняются в директории logs_tg_bot.
"""
import logging
from logging.handlers import RotatingFileHandler

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)s'


def logger_get(name):
    logger_name = logging.getLogger(name)
    return logger_name


file_handler = logging.handlers.RotatingFileHandler(
    filename='logs_tg_bot.log',
    maxBytes=1000
)
file_handler.setLevel(logging.INFO)  # задаем уровень логгирования
file_handler.setFormatter(logging.Formatter(log_format))
logger = logger_get(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
