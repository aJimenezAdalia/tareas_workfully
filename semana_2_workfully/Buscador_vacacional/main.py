

from classes import GetHolidayInfo
from utils import read_config_file, save_image, resize_image
import os
import shutil
import json


def main():
    # Config file path
    yml_path = os.getcwd() + '/config.yml'
    # Config dictionary
    config_dict = read_config_file(path=yml_path)

    # Getting required parameters from yaml config file
    city = config_dict['destination_city']
    country_code = config_dict['destination_country_code']
    number_of_images = config_dict.get('image_params')[0].get('number_of_images')
    image_size = tuple([int(config_dict.get('image_params')[0].get('image_width')),
                       int(config_dict.get('image_params')[0].get('image_height'))])
    number_of_news = config_dict.get('news_params')[0].get('number_of_news')
    avg_temp = config_dict.get('weather_params')[0].get('temperature')

    # 1. Getting Data -----------------------------------------------------------

    # 1.1. Creating GetHolidayInfo object
    info_getter = GetHolidayInfo(
        destination_city=city,
        destination_country_code=country_code,
        destination_type='Urban')

    # 1.2. Get images URLs
    image_URLS = info_getter.get_images(number_of_images=number_of_images)

    # 1.3. Get News data
    news_data = info_getter.get_news(number_of_news=number_of_news)

    # 1.4. Get Weather data
    weather_data = info_getter.get_weather()

    # 2. Directories ----------------------------------------------------------

    # 2.1. Creating root directory —removing first if already exists.
    folder_name = city.lower() + '_folder/'

    if folder_name in os.listdir() or folder_name[:-1] in os.listdir():
        shutil.rmtree(folder_name)
        os.mkdir(folder_name)
    else:
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            pass

    # 2.2. Creating images directory
    img_dir_name = folder_name + city + '_images/'
    try:
        os.mkdir(img_dir_name)
    except FileExistsError:
        pass

    # 2.3. Creating data directory
    data_dir_name = folder_name + city + '_other_data/'
    try:
        os.mkdir(data_dir_name)
    except FileExistsError:
        pass

    # 3. Storing data ----------------------------------------------------------

    # 3.1. Saving images (URL to local)
    for pos, image_url in enumerate(image_URLS):
        save_image(image_url, img_dir_name, city + '_' + str(pos+1))

    # 3.2. Creating JSON File
    json_data = {}
    json_data['weather_forecast'] = weather_data
    json_data['destination_news'] = news_data

    # 3.3. Saving JSON File
    if ' ' in city: # we don't want whitespaces in our JSON file name
        city = city.replace(' ', '_')
    with open(data_dir_name + f'{city}_data.json', 'w') as write_file:
        json.dump(json_data, write_file)

    # 3.4. Resizing images
    os.chdir(img_dir_name)
    for image in os.listdir():
        resize_image(image, image_size)

    # 3.5. Removing original images
    for image in os.listdir():
        if not image.startswith('resiz'):
            os.remove(image)


if __name__ == "__main__":
    main()




