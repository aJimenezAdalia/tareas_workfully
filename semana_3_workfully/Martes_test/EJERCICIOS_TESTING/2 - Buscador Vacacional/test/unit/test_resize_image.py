

import unittest
from PIL import Image
from src.utils import resize_image

class TestResizeImage(unittest.TestCase):

    # Wrong path - FileNotFoundError expected
    def test_resize_image_path(self):
        with self.assertRaises(FileNotFoundError):
            resize_image(image_path='google.es',
                         image_size=(150, 90))

    # Invalid size - FileNotFoundError expected
    def test_resize_image_size(self):
        with self.assertRaises(FileNotFoundError):
            resize_image(image_path='google.es',
                         image_size=True)



if __name__ == '__main__':
    unittest.main()