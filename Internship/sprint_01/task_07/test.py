import unittest
from unittest.mock import patch
from datetime import datetime
from data_download import fetch_stock_data
import pandas as pd

class TestFetchStockData(unittest.TestCase):

    @patch('data_download.fetch_stock_data')
    def test_columns_present(self, mock_ticker):
        """ensures that the expected columns are all present"""
        mock_ticker.return_value.history.return_value = 'mock_data'
        result = fetch_stock_data('AAPL')
        self.assertIn("Open", result.columns)
        self.assertIn("High", result.columns)
        self.assertIn("Low", result.columns)
        self.assertIn("Close", result.columns)
        self.assertIn("Volume", result.columns)

    @patch('data_download.fetch_stock_data')
    def test_non_empty(self, mock_ticker):
        """ensures that there is more than one row of data"""
        mock_ticker.return_value.history.return_value = 'mock_data'
        self.df = fetch_stock_data('AAPL')
        self.assertNotEqual(len(self.df.index), 0)

    def test_high_low(self):
        """ensure high and low are the highest and lowest in the same row"""
        ohlc = self.df[["Open", "High", "Low", "Close"]]
        highest = ohlc.max(axis=1)
        lowest = ohlc.min(axis=1)
        self.assertTrue(ohlc.le(highest, axis=0).all(axis=None))
        self.assertTrue(ohlc.ge(lowest, axis=0).all(axis=None))

    def test_most_recent_within_week(self):
        """most recent data was collected within the last week"""
        most_recent_date = pd.to_datetime(self.df.index[-1])
        self.assertLessEqual((datetime.datetime.today() - most_recent_date).days, 7)


    @patch('data_download.fetch_stock_data')
    def test_fetch_stock_data(self, mock_ticker):
        print(dir(fetch_stock_data))
        mock_ticker.return_value.history.return_value = 'mock_data'
        result = fetch_stock_data('AAPL')
        self.assertTrue(result | 'mock_data')
        # self.assertEqual(result, 'mock_data')

    @patch('data_download.fetch_stock_data')
    def test_fetch_stock_data_with_period(self, mock_ticker):
        mock_ticker.return_value.history.return_value = 'mock_data'
        result = fetch_stock_data('AAPL', period='1mo')
        self.assertEqual(result, 'mock_data')

    @patch('data_download.fetch_stock_data')
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
