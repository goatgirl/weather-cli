import api_data


class Weather(object):

    def __init__(self, location, config):
        data = Weather.lookup(location, config)
        self.summary = data['currently']['summary']
        self.temperature = data['currently']['temperature']
        self.forecast = data['daily']['summary']
        self.icon = data['currently']['icon']

    @staticmethod
    def lookup(location, config):
        url = config.weather_url.format(
            key=config.api_key,
            lat=location.latitude,
            lng=location.longitude
        )
        return api_data.fetch(url)

