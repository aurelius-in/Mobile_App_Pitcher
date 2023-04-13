import pandas as pd
import os
import unittest
from src.data_collection import process_raw_data, clean_app_ideas

class TestDataCollection(unittest.TestCase):
    def test_process_raw_data(self):
        # test that processed data file exists
        self.assertTrue(os.path.exists(os.path.join("data", "processed_data", "investor_data.csv")))

        # test that processed data has the expected number of rows
        processed_data = pd.read_csv(os.path.join("data", "processed_data", "investor_data.csv"))
        self.assertEqual(len(processed_data), 10)

    def test_clean_app_ideas(self):
        # test that cleaned app ideas file exists
        self.assertTrue(os.path.exists(os.path.join("data", "processed_data", "app_ideas.csv")))

        # test that cleaned app ideas has the expected number of rows
        app_ideas_data = pd.read_csv(os.path.join("data", "processed_data", "app_ideas.csv"))
        self.assertEqual(len(app_ideas_data), 5)

if __name__ == '__main__':
    unittest.main()
