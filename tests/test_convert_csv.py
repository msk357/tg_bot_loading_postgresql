import os
import sys
import unittest
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tg_bot')))

from tg_bot.convert_csv  import (
    converts_columns_percentages,
    converts_columns_date,
    converts_columns_address
)


# переменные для тестирования функции converts_columns_percentages
percent_to_int_valid: dict[str] = {'percent_to_int': ['50%']}
percent_to_int_not_valid: dict[str] = {'percent_to_int': ['not valid format']}

# переменные для тестирования функции converts_columns_date
column_date_valid: dict[str] = {'column_date': ['11.01.2023']}
column_date_not_valid: dict[str] = {'column_date': ['not valid format']}

# переменные для тестирования функции converts_columns_date
column_address_valid: dict[str] = {'address_id': ['Горьковское2 *Теле2* (ВИ)']}
column_address_int: dict[str] = {'address_id': [1]}


class TestConvertCsv(unittest.TestCase):

    """Тест проверяет результат при передаче валидных данных"""
    def test_converts_columns_percentages(self):
        df = pd.DataFrame(percent_to_int_valid)
        table_context = {'percent_to_int': ['percent_to_int']}
        result_df = converts_columns_percentages(df, table_context)
        self.assertEqual(result_df['percent_to_int'][0], 0.5)

    """Тест проверяет результат при передаче данных типа str"""
    def test_converts_columns_percentages_not_valid(self):
        with self.assertRaises(ValueError):  # функция ождидает тип float
            df = pd.DataFrame(percent_to_int_not_valid)
            table_context = {'percent_to_int': ['percent_to_int']}
            converts_columns_percentages(df, table_context)

    """Тест проверяет результат при передаче валидных данных"""
    def test_converts_columns_date(self):
        df = pd.DataFrame(column_date_valid)
        table_context = {'column_date': ['column_date']}
        result_df = converts_columns_date(df, table_context)
        self.assertEqual(result_df['column_date'][0], '2023-11-01')

    """Тест проверяет результат при передаче данных типа str"""
    def test_converts_columns_date_not_valid(self):
        with self.assertRaises(ValueError):  # функция ождидает тип date
            df = pd.DataFrame(column_date_not_valid)
            table_context = {'column_date': ['column_date']}
            converts_columns_date(df, table_context)

    """Тест проверяет результат при передаче валидных данных"""
    def test_converts_columns_address_valid(self):
        df = pd.DataFrame(column_address_valid)
        table_context = {'address_id': ['address_id']}
        result_df = converts_columns_address(df, table_context)
        self.assertEqual(result_df['address_id'][0], 'Горьковское2 *Теле2* (ВИ)')

    """Тест проверяет результат при передаче данных типа int"""
    def test_converts_columns_address_int(self):
        with self.assertRaises(ValueError) as error:  # функция ождидает тип str
            df = pd.DataFrame(column_address_int)
            table_context = {'address_id': ['address_id']}
            converts_columns_address(df, table_context)
        self.assertEqual('В колонке с адресом точки переданы данные формата int', error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
