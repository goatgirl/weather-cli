import config
import api_data


class Weather(object):

    def __init__(self, location):
        data = Weather.lookup(location)
        self.summary = data['currently']['summary']
        self.temperature = data['currently']['temperature']
        self.forecast = data['daily']['summary']

    @staticmethod
    def lookup(location):
        url = config.weather_url.format(
            key=config.weather_key,
            lat=location.latitude,
            lng=location.longitude
        )
        return api_data.fetch(url)



