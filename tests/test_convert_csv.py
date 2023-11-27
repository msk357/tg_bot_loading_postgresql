import unittest
import pandas as pd

from tg_bot.convert_csv import converts_columns_percentages


class TestConvertCsv(unittest.TestCase):
    def test_converts_columns_percentages(self):
        df = pd.DataFrame({
            'percent_to_int': ['50%']
        })
        table_context = {'percent_to_int': ['percent_to_int']}
        result_df = converts_columns_percentages(df, table_context)
        self.assertEqual(result_df['percent_to_int'][0], 0.5)


if __name__ == 'main':
    unittest.main()
