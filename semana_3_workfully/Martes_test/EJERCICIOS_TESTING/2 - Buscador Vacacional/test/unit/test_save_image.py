

import unittest
import urllib
from src.utils import save_image

class TestSaveImage(unittest.TestCase):

    # Empty path - IndexError expected
    def test_save_image_path(self):
        with self.assertRaises(IndexError):
            save_image(url='google.es',
                       path='',
                       image_name='image name')

    # Invalid URL - AttributeError expected
    def test_save_image_url(self):
        with self.assertRaises(AttributeError):
            save_image(url=1245,
                       path='my_path',
                       image_name='image name')



if __name__ == '__main__':
    unittest.main()