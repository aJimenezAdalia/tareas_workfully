

import unittest
import pandas as pd
from src.utils import get_dataframe

class TestGetDataframe(unittest.TestCase):

    # Wrong data input
    def test_dataframe_type(self):
        result = get_dataframe(True)
        self.assertEqual(type(result), pd.DataFrame)

    # ValueError
    def test_dataframe_value_error(self):
        with self.assertRaises(ValueError):
            get_dataframe(True)


if __name__ == '__main__':
    unittest.main()