

import unittest
from src.utils import get_data

class TestGetData(unittest.TestCase):

    # No token, must raise FileNotFoundError
    def test_no_token(self):
        with self.assertRaises(FileNotFoundError):
            get_data(True, True)

if __name__ == '__main__':
    unittest.main()