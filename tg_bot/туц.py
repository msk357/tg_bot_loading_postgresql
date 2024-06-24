import re


z = 'chudinova_darya_den - =cx'


def split_string(s):
    # Используем регулярное выражение для разделения строки по позициям,
    # где следующий символ не является алфавитным и не равно '_'.
    pattern = r'(?<=\D)(?=[^a-zA-Z_])'
    return re.split(pattern, s)[0]


print(split_string(z))
