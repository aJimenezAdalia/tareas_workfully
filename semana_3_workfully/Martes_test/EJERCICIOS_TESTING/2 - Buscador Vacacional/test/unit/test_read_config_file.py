

import unittest
from PIL import Image
from src.utils import read_config_file

class TestReadYaml(unittest.TestCase):

    # Wrong path - Must return "File Not Found."
    def test_read_config(self):
        result = "File Not Found."
        self.assertEqual(read_config_file(''), result)

if __name__ == '__main__':
    unittest.main()