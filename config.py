import sys

import file


class Config(object):

    def __init__(self):
        self.load()

    def load(self):
        if file.exists('settings.py'):
            config = file.read_json('settings.py')
            self.save_file = config['save-file']
            self.location_url = config['location-url']
            self.weather_url = config['weather-url']
            if 'weather-key' in config:
                self.weather_key = config['weather-key']

    def save(self, key):
        config = {
            'location-url':
            'https://maps.googleapis.com/maps/api/geocode/json?address={loc}',
            'save-file': 'weather.sav',
            'weather-url':
            'https://api.darksky.net/forecast/{key}/{lat},{lng}?units=uk2'
        }
        if key:
            config.update({"weather-key": key})
            print(config)
            sys.exit()
        file.save_json('settings.py', config)


def save_config(key=None):
    print("Save key function moved to Config class")
    # config = {
    #     'location-url':
    #     'https://maps.googleapis.com/maps/api/geocode/json?address={loc}',
    #     'save-file': 'weather.sav',
    #     'weather-url':
    #     'https://api.darksky.net/forecast/{key}/{lat},{lng}?units=uk2',
    # }
    # if key:
    #     config.update({"weather-key": key})
    #     print(config)
    #     sys.exit()
    # file.save_json('settings.py', config)


# if file.exists('settings.py'):
#     config = file.read_json('settings.py')
#     if 'weather-key' in config:
#         save_file = config['save-file']
#         location_url = config['location-url']
#         weather_url = config['weather-url']
#         weather_key = config['weather-key']
#     else:
#         print('Add darksky API with command: python main.py -k <API KEY>')
#         # print("API key can be obtained from https://darksky.net/dev/")
# else:
#     save_config()
#     print("creating settings file")
#     sys.exit()

