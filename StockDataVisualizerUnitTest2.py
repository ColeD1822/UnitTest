import unittest
import datetime
from StockDataVisualizer import main


class StockDataVisualizerTest(unittest.TestCase):
    def setUp(self):
        self.stock_symbol = "GOOGL"
        self.chart_type = "1"
        self.time_series = "4"
        self.start_date = "2022-01-01"
        self.end_date = "2022-12-31"

    def test_symbol(self):
        self.assertTrue(self.stock_symbol.isalpha())
        self.assertTrue(self.stock_symbol.isupper())
        self.assertGreaterEqual(len(self.stock_symbol), 1)
        self.assertLessEqual(len(self.stock_symbol), 7)
    
    def test_chart_type(self):
        self.assertTrue(self.chart_type.isnumeric())
        self.assertIn(self.chart_type, ["1", "2"])
    
    def test_time_series(self):
        self.assertTrue(self.time_series.isnumeric())
        self.assertIn(self.time_series, ["1", "2", "3", "4"])
    
    def test_start_date(self):
        try:
            datetime.datetime.strptime(self.start_date, "%Y-%m-%d")
        except Exception as e:
            print(f"Start Date Error. Check for correct format. {e}")
    
    def test_end_date(self):
        try:
            datetime.datetime.strptime(self.end_date, "%Y-%m-%d")
        except Exception as e:
            print(f"End Date Error. Check for correct format. {e}")

unittest.main()