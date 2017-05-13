import api_data


class Location(object):

    def __init__(self, address, location_url):
        self.address = None
        self.latitude = None
        self.longitude = None
        self.lookup(address, location_url)

    def lookup(self, address, location_url):
        url = location_url.format(loc=api_data.url_safe(address))
        data = api_data.fetch(url)
        if data['status'] == 'ZERO_RESULTS':
            self.address = None
            print('Location: address not found')
        else:
            result = data['results'][0]
            self.address = (result['formatted_address'])
            self.latitude = (result['geometry']['location']['lat'])
            self.longitude = (result['geometry']['location']['lng'])
