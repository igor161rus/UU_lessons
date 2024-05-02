import unittest
from unittest.mock import patch
from datetime import datetime
from data_download import fetch_stock_data


class TestFetchStockData(unittest.TestCase):

    @patch('data_download.fetch_stock_data')
    def test_fetch_stock_data(self, mock_ticker):
        print(dir(fetch_stock_data))
        mock_ticker.return_value.history.return_value = 'mock_data'
        result = fetch_stock_data('AAPL')
        self.assertEqual(result, 'mock_data')

    @patch('data_download.yfinance.Ticker')
    def test_fetch_stock_data_with_period(self, mock_ticker):
        mock_ticker.return_value.history.return_value = 'mock_data'
        result = fetch_stock_data('AAPL', period='1mo')
        self.assertEqual(result, 'mock_data')

    @patch('data_download.yfinance.Ticker')
    def test_fetch_stock_data_with_dates(self, mock_ticker):
        mock_ticker.return_value.history.return_value = 'mock_data'
        result = fetch_stock_data('AAPL', date_start='2020-01-01', date_end='2020-01-02')
        self.assertEqual(result, 'mock_data')

    def test_fetch_stock_data_invalid_period(self):
        with self.assertRaises(ValueError):
            fetch_stock_data('AAPL', period='invalid_period')

    def test_fetch_stock_data_start_after_end(self):
        with self.assertRaises(ValueError):
            fetch_stock_data('AAPL', date_start='2020-01-02', date_end='2020-01-01')


if __name__ == '__main__':
    unittest.main()
