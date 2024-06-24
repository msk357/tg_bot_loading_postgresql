"""
Модуль для обработки CSV-файлов перед загрузкой в DB.
В переменной NAME_COLUMN_FOR_CONVERT выделены три основных типа данных.
column_date - колонки с датой, функция устанавливает тип даты %Y-%m-%d.
column_int - колонки с цифрами, функция убирает значения после разделителя.
percent_to_int - колонки с процентами, приводятся к цисловому формате типа numeric.

Функция convert_column осуществляет основную логику обработки данных в CSV.
Ожидаемый ввод - датафрейм и переменная context с словарем.
"""
import pandas as pd
import re

from settings import (
    CURRENT_PK_INT,
    CURRENT_PK_STR,
    COLUMNS_NAME_POSID_IN_CSV,
    CSV_CONVERSION_FROM_UNPIVOT,
    PATH_DIRECTORY
)


"""
Функция для обработки CSV-файла принимает ключи из словаря TABLES_LIST_DB.
На основании ключей проводится обработка CSV-файла и соответствующих полей.
"""


"""Функция подготавливает колонки, с данными типа date"""


def converts_columns_date(df, table_context: dict[str]):
    # обработка полей с типом дата
    try:
        for i in range(len(table_context['column_date'])):
            time: str = table_context['column_date'][i]  # сохраняем название столбца в переменную
            df[time] = df[time].replace('NULL', '')  # заменяем значения NULL
            df[time] = pd.to_datetime(df[time]).dt.strftime('%Y-%m-%d')  # преобразуем дату в формат YY-MM-DD
        return df
    except Exception as error:
        raise ValueError(f'Проверьте столбцы с датой в загружаемой таблице: \n {error}')


"""Функция конвертирует колонки с PK в формате str"""


def converts_columns_address(df, table_context: dict[str]):
    if df[table_context['address_id'][0]].dtypes in ['int', 'int64', 'float']:
        raise ValueError('В колонке с адресом точки переданы данные формата int')
    else:
        df[table_context['address_id'][0]] = df[table_context['address_id'][0]].map(
            lambda x: x if x in CURRENT_PK_STR else 'нет адреса'
        )  # если PK нет в списке CURRENT_PK_STR, значение заменяется на 'нет адреса'
        df = df[df[table_context['address_id'][0]] != 'нет адреса']  # удаляются значения 'нет адреса'
        return df


"""Функция конвертирует колонки с данными типа процент"""


def converts_columns_percentages(df, table_context: dict[str]):
    # обработка полей с типом percent, приведение к типу numeric в БД
    try:
        for i in range(len(table_context['percent_to_int'])):
            # преобразуем процент в число за счёт замены % на '' и деления на 100
            df[table_context['percent_to_int'][i]] = (
                df[table_context['percent_to_int'][i]].map(
                    lambda x:
                    float(str(x).replace('%', '').replace(',', '.')) / 100
                    if pd.notnull(x) and x != '' and x != 'NULL' else x
                )
            )
        return df
    except Exception as error:
        raise ValueError(f'Проверьте столбцы с процентами в загружаемой таблице: \n {error}')


"""Функция конвертирует колонки, где в качестве разделителя используется ;"""


def converts_columns_separations(df, table_context: dict[str]):
    for i in range(len(table_context['separations'])):
        df[table_context['separations'][i]] = (
            df[table_context['separations'][i]].map(
                lambda x: str(x).replace(';', '.')
            )
        )  # заменяем ; на . в строках таблицы CSV
    return df


"""Функция удаляет пустые строки после данных ячейке"""


def del_empty_lines(df, table_context: dict[str]):
    pattern = r'(?<=\D)(?=[^a-zA-Z_])'
    for i in range(len(table_context['empty_lines'])):
        df[table_context['empty_lines'][i]] = (
            df[table_context['empty_lines'][i]].map(
                lambda x: re.split(pattern, str(x))[0]
            )
        )  # сохраняем данные до пробела
    return df


"""Функция конвертирует колонки с типом int"""


def converts_columns_int(df, table_context: dict[str]):
    for i in range(len(table_context['column_int'])):
        # проверка на поле типа pos_id
        if table_context['column_int'][i] in COLUMNS_NAME_POSID_IN_CSV:
            df[table_context['column_int'][i]] = (
                df[table_context['column_int'][i]].
                map(lambda x: int(str(x).replace(',', '.')
                                  .split('.')[0]) if pd.notnull(x) and x in CURRENT_PK_INT else 0)
            )  # если PK нет в списке CURRENT_PK_INT, значение заменяется на 0
            df = df[df[table_context['column_int'][i]] != 0]  # удаляем строки с PK равным 0
            df[table_context['column_int'][i]] = df[table_context['column_int'][i]].astype(int)

        else:
            df[table_context['column_int'][i]] = (
                df[table_context['column_int'][i]].
                map(lambda x: int(str(x).replace(',', '.').
                                  split('.')[0]) if pd.notnull(x) and x != 'NULL' else None)
            )  # преобразуем значение в str, заменяем , на . и сохраняем только целое значение

    return df


"""
Функция считывает контекст словаря TABLES_LIST_DB и запускает процесс обработки CSV-файла.
В качестве аргумента функция принимаем датафрейм и контекст словаря с названием колонок.
"""


def converts_columns(df, table_context: dict[str]):
    if 'column_int' in table_context:
        df = converts_columns_int(df, table_context)
    if 'separations' in table_context:
        df = converts_columns_separations(df, table_context)
    if 'percent_to_int' in table_context:
        df = converts_columns_percentages(df, table_context)
    if 'column_date' in table_context:
        df = converts_columns_date(df, table_context)
    if 'address_id' in table_context:
        df = converts_columns_address(df, table_context)
    if 'empty_lines' in table_context:
        df = del_empty_lines(df, table_context)
    return df


"""
Функция для подготовки CSV-файлов.
Определяется наличие поля date и устанавливает значение по умолчанию.
Тип поля "число" - заменяется разделитель , на .
Тип поля "дата" - формат "YYYY-MM-DD".
"""


def convert_csv_data(name_table_for_load: str, table_context: dict[str]) -> None:
    # ветвление для преобразования из сводной таблицы CSV в обычный формат
    if name_table_for_load in CSV_CONVERSION_FROM_UNPIVOT:
        df_unpivot = pd.read_csv(
            f'{PATH_DIRECTORY}{name_table_for_load}.csv',
            delimiter=';'
        )
        # указываем названия столбцов для создания строковой таблицы
        df_unpivot = df_unpivot.melt(id_vars=['Код ТТ'], var_name='DATE', value_name='VALUE')
        df_unpivot.to_csv(f'{PATH_DIRECTORY}{name_table_for_load}.csv', index=False, sep=';')

        df = pd.read_csv(
            f'{PATH_DIRECTORY}{name_table_for_load}.csv',
            delimiter=';',
            parse_dates=[*table_context['column_date']],
            dayfirst=True
        )
        df = converts_columns(df, table_context)
        df_for_load = df[table_context['columns_name_csv']]
        df_for_load.to_csv(f'{PATH_DIRECTORY}{name_table_for_load}.csv', index=False, sep=';')

    # обработка CSV с колонкой формата "дата"
    elif 'column_date' in table_context:
        df = pd.read_csv(
            f'{PATH_DIRECTORY}{name_table_for_load}.csv',
            delimiter=';',
            parse_dates=[*table_context['column_date']],
            dayfirst=True
        )
        df = df.fillna('NULL')  # заменяем пустые ячейки на null
        df = converts_columns(df, table_context)
        df_for_load = df[table_context['columns_name_csv']]
        df_for_load.to_csv(f'{PATH_DIRECTORY}{name_table_for_load}.csv', index=False, sep=';')

    # обработка CSV без колонки с датой
    else:
        df = pd.read_csv(
            f'{PATH_DIRECTORY}{name_table_for_load}.csv',
            delimiter=';',
            dayfirst=True
        )
        df = df.fillna('NULL')
        df = converts_columns(df, table_context)
        df_for_load = df[table_context['columns_name_csv']]
        df_for_load.to_csv(f'{PATH_DIRECTORY}{name_table_for_load}.csv', index=False, sep=';')

    return
