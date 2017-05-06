# enc_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=huddersfield%20west%20yorkshire'

import requests
from urllib.parse import quote


def geocode(location):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}'
    enc_url = url.format(quote(location))
    return requests.get(url=enc_url).json()


data = geocode('huddersfield west yorkshire')

print('Address:', data['results'][0]['formatted_address'])
print('latitude:', data['results'][0]['geometry']['location']['lat'])
print('longitude:', data['results'][0]['geometry']['location']['lng'])
