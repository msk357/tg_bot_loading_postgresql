"""
Модуль для подключения к DB и загрузки данных из CSV.
Укажите путь к файлу CSV и данные для подключения к DB в settings.py.
Основная переменная TABLES_LIST_DB, в ней хранится вводная информация для работы с CSV и БД.
"""
import psycopg2

from settings import DATABASE, USER_DB, PASSWORD, HOST, PORT, TABLES_LIST_DB


"""
Функция для загрузки данных в PostgreSQL из CSV-файла.
Для загрузки данных создается временная таблица, из которой копируются данные в
основную таблицу DB. В переменную conn необходимо внести данные DB для подключения.
database - название DB,
user - название пользователя (проверьте права пользователя в DB),
password - пароль для подключения к DB,
host - IP-адрес для подключения к DB,
port - порт, через который проходит подключение к DB.
"""


def load_csv_db(path_directory: str, name_table_db: str) -> None:
    # в переменную conn добавляются данные для подключения к DB
    conn = psycopg2.connect(database=DATABASE,
                            user=USER_DB,
                            password=PASSWORD,
                            host=HOST,
                            port=PORT
                            )
    cur = conn.cursor()

    # сохраняем в переменную название колонки PK и названия обновляемых колонок
    id_load: str = ', '.join([*TABLES_LIST_DB[name_table_db]['table_id']])
    columns_load_str: str = ', '.join([*TABLES_LIST_DB[name_table_db]['columns_name_db']])
    # переменная name_temp_table назначает имя временной таблицы БД
    name_temp_table: str = 'temp_table'

    # создаем временную таблицу
    create_temp_table: str = (f"CREATE TEMP TABLE {name_temp_table} "
                              f"AS SELECT * FROM {name_table_db} "
                              f"WHERE  1 = 0")
    cur.execute(create_temp_table)

    # Загрузка данных из CSV файла во временную таблицу
    with open(f'{path_directory}{name_table_db}.csv', 'r') as f:
        next(f)
        cur.copy_from(f, f'{name_temp_table}', sep=';', null='NULL')

    # Загрузка только уникальных записей из временной таблицы в основную таблицу
    insert_unique_query: str = (f"INSERT INTO {name_table_db} ({columns_load_str}) "
                                f"SELECT {columns_load_str} "
                                f"FROM {name_temp_table} "
                                f"WHERE NOT EXISTS "
                                f"(SELECT 1 FROM {name_table_db} "
                                f"WHERE {name_table_db}.{id_load} = {name_temp_table}.{id_load})")

    cur.execute(insert_unique_query)
    conn.commit()
    conn.close()
    return
