

import requests
import urllib

# Class GetHolidayInfo
class GetHolidayInfo:
    """Contains methods to get info from a concrete destination city"""

    def __init__(self, destination_city, destination_country_code, destination_type):
        """Class constructor. Defines the city and country

        Params:
            - destination_city: str, destination city
            - destination_country_code: str, code of the destination country
        """
        self.destination_city = destination_city.lower()
        self.destination_country_code = destination_country_code.lower()
        self.destination_type = destination_type

    def get_images(self, number_of_images):
        """Get a provided number of images from Google API.

        Params:
            - number_of_images: int, number of images to get from Google API

        Return:
            - image_urls: list, list of URLs where the images are stored
        """

        # Google Images API Parameters

        url = "https://google-search3.p.rapidapi.com/api/v1/images/"
        headers = {
            'x-user-agent': "desktop",
            'x-proxy-location': "EU",
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "1ca795b67amshfa6cf81e0962bf1p1e245ajsn33f3f8989a97"}

        # Query
        query = {"q": self.destination_city, "num": number_of_images}

        # API Response
        response = requests.get(url + urllib.parse.urlencode(query), headers=headers)
        response_json = response.json()


        # Getting image URLs
        image_list = response_json['image_results']
        image_urls = []  # Will contain the images URLs

        for image_info in image_list:
            image_url = image_info.get('image').get('src')
            image_urls.append(image_url)

        return image_urls

    def get_news(self, number_of_news):
        """Get a provided number of news from News Search API.

        Params:
            - number_of_news: int, number of news to get from API.

        Return:
            - full_news: list, list of requested news
        """

        # News Search API Parameters
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"

        city = self.destination_city
        news_number = number_of_news

        querystring = {"q": city, "pageNumber": "1", "pageSize": str(news_number), "autoCorrect": "true",
                       "fromPublishedDate": "null", "toPublishedDate": "null"}

        headers = {
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
            'x-rapidapi-key': "1ca795b67amshfa6cf81e0962bf1p1e245ajsn33f3f8989a97"
        }

        # API Response
        response = requests.request("GET", url, headers=headers, params=querystring)
        news_json = response.json()

        # Getting requested news
        news_list = news_json.get('value')
        full_news = []  # Will contain the main news

        for new_info in news_list:
            title = new_info['title']
            full_news.append(title)

        return full_news

    def get_weather(self):
        """Returns weather forecast from Open Weather Map API"""

        # API Parameters
        url = "https://community-open-weather-map.p.rapidapi.com/forecast"
        city = self.destination_city
        country_code = self.destination_country_code

        querystring = {"q": city + ", " + country_code}
        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "1ca795b67amshfa6cf81e0962bf1p1e245ajsn33f3f8989a97"
        }

        # API Response
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_json = response.json()

        # Parameters list
        params_list = response_json.get('list')
        day_1_data = params_list[0]
        day_2_data = params_list[8]
        day_3_data = params_list[16]

        weather_list = []  # Will contains forecasting for the next three days

        for pos, day_data in enumerate([day_1_data, day_2_data, day_3_data]):
            day = 'day_' + str(pos + 1)
            day_forecast = {}
            temperature = day_data.get('main').get('temp')
            sky_condition = day_data.get('weather')[0].get('main')
            day_forecast[day] = {'temperature': temperature, 'sky_condition': sky_condition}
            weather_list.append((day_forecast))

        return weather_list

    def get_customized_info(self):
        """Based on destination_type, the user will receive customized
        recommendations to his travel (webs, links of interest...)"""
        # To implement in the future
        pass



