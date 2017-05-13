import api_data


class Weather(object):

    def __init__(self, location, config):
        data = Weather.lookup(location, config)
        self.now = data['currently']
        self.day = []
        for i in range(2):
            self.day.append(data['daily']['data'][i])

    @staticmethod
    def lookup(location, config):
        url = config.weather_url.format(
            key=config.api_key,
            lat=location.latitude,
            lng=location.longitude
        )
        return api_data.fetch(url)
