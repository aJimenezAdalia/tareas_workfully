

import os
import urllib
import yaml
from PIL import Image


def save_image(url, path, image_name):
    """Save an image from the provided url"""
    image_name = image_name + '.jpg'

    # Validating path
    if path[-1] not in ['/', '\\']:
        path += '/'
    path = path.replace('\\', '/')

    full_path = path + image_name

    # Saving image in provided path
    urllib.request.urlretrieve(url, full_path)


def resize_image(image_path, image_size=(150, 90)):
    """Resize a image"""
    img = Image.open(image_path)
    new_size = image_size
    img = img.resize(new_size, Image.ANTIALIAS)

    img_name = 'resized_' + image_path
    img.save(img_name, format='JPEG')


def read_config_file(path, file_name='config.yml'):
    """Read yml config file to get parameters

    Params:
        - path: str, path where the yml is located (local)
        - file_name: str, default: 'config.yml', name of the yml file
    Return:
        - parsed_yml: dict, yml paramaters
    """
    try:
        if 'config.yml' in os.listdir():
            config_file = 'config.yml'
        else:
            config_file = path + file_name

        with open(config_file, 'r') as stream:
            parsed_yml = yaml.safe_load(stream)
            return parsed_yml
    except FileNotFoundError:
        print("File Not Found.")