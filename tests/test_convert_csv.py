import unittest
import pandas as pd

from tg_bot.convert_csv import converts_columns_percentages, converts_columns_date, converts_columns_address


# переменные для тестирования функции converts_columns_percentages
percent_to_int: dict[str] = {'percent_to_int': ['50%']}
percent_to_int_not_valid: dict[str] = {'percent_to_int': ['not valid format']}

# переменные для тестирования функции converts_columns_date
column_date: dict[str] = {'column_date': ['11.01.2023']}
column_date_not_valid: dict[str] = {'column_date': ['not valid format']}


class TestConvertCsv(unittest.TestCase):
    def test_converts_columns_percentages(self):
        df = pd.DataFrame(percent_to_int)
        table_context = {'percent_to_int': ['percent_to_int']}
        result_df = converts_columns_percentages(df, table_context)
        self.assertEqual(result_df['percent_to_int'][0], 0.5)

    def test_converts_columns_percentages_not_valid(self):
        with self.assertRaises(ValueError):
            df = pd.DataFrame(percent_to_int_not_valid)
            table_context = {'percent_to_int': ['percent_to_int']}
            converts_columns_percentages(df, table_context)

    def test_converts_columns_date(self):
        df = pd.DataFrame(column_date)
        table_context = {'column_date': ['column_date']}
        result_df = converts_columns_date(df, table_context)
        self.assertEqual(result_df['column_date'][0], '2023-11-01')

    def test_converts_columns_date_not_valid(self):
        with self.assertRaises(ValueError):
            df = pd.DataFrame(column_date_not_valid)
            table_context = {'column_date': ['column_date']}
            converts_columns_date(df, table_context)


if __name__ == 'main':
    unittest.main()
