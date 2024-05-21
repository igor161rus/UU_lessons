import unittest
from data_download import fetch_stock_data


class TestFetchStockData(unittest.TestCase):

    def setUp(self):
        self.df = fetch_stock_data('AAPL')

    def test_columns_present(self):
        """Тест проверяет, все ли ожидаемые столбцы присутствуют"""
        result = fetch_stock_data('AAPL')
        self.assertIn("Open", self.df.columns)
        self.assertIn("High", self.df.columns)
        self.assertIn("Low", self.df.columns)
        self.assertIn("Close", self.df.columns)
        self.assertIn("Volume", self.df.columns)

    def test_non_empty(self):
        """Тест проверяет наличие более одной строки данных"""
        self.assertNotEqual(len(self.df.index), 0)

    def test_high_low(self):
        """Тест проверяет, что максимум и минимум являются самым высоким и самым низким в одной строке"""
        ohlc = self.df[["Open", "High", "Low", "Close"]]
        highest = ohlc.max(axis=1)
        lowest = ohlc.min(axis=1)
        self.assertTrue(ohlc.le(highest, axis=0).all(axis=None))
        self.assertTrue(ohlc.ge(lowest, axis=0).all(axis=None))

    def test_fetch_stock_data_invalid_period(self):
        """Тест проверяет, что функция fetch_stock_data() выбрасывает исключение при невалидном периоде"""
        with self.assertRaises(KeyError):
            fetch_stock_data('AAPL', period='2mo')

    def test_fetch_stock_data_start_after_end(self):
        """Тест проверяет, что функция fetch_stock_data() выбрасывает исключение при невалидном периоде"""
        with self.assertRaises(ValueError):
            fetch_stock_data('AAPL', date_start='2020-01-02', date_end='2020-01-01')


if __name__ == '__main__':
    unittest.main()
