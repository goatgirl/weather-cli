import file


class Config(object):

    def __init__(self):
        self.api_key = None
        self.default_location = None
        self.location_url =\
            'https://maps.googleapis.com/maps/api/geocode/json?address={loc}'
        self.save_file = 'data.sav'
        self.weather_url =\
            'https://api.darksky.net/forecast/{key}/{lat},{lng}?units=uk2'
        self.load()

    def __str__(self):
        return "{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}".format(
                'api_key', self.api_key,
                'default_location', self.default_location,
                'location_url', self.location_url,
                'save_file', self.save_file,
                'weather_url', self.weather_url
        )

    def load(self):
        if file.exists(self.save_file):
            data = file.read_json(self.save_file)
            if data['api_key']:
                self.api_key = data['api_key']
            if data['default_location']:
                self.default_location = data['default_location']

    def save(self, key, location):
        if key:
            self.api_key = key
            data = {
                'api_key': key,
                'default_location': location
            }
            file.save_json(self.save_file, data)
