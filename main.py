# enc_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=huddersfield%20west%20yorkshire'

import requests
from urllib.parse import quote

import settings


def geocode(location):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}'
    enc_url = url.format(quote(location))
    return requests.get(enc_url).json()


def weather(latitude, longitude):
    url = settings.weather['url'].format(
        key=settings.weather['key'],
        lat=latitude,
        lng=longitude
    )
    return requests.get(url).json()


def f2c(f):
    return int((f - 32) * 5 / 9)


geo = geocode('hebdon bridge west yorkshire')

lat = geo['results'][0]['geometry']['location']['lat']
lng = geo['results'][0]['geometry']['location']['lng']

data = weather(lat, lng)

print('Address:', geo['results'][0]['formatted_address'])
print('Summary:', data['currently']['summary'])
print('Temperature: {}\xb0C'.format(f2c(data['currently']['temperature'])))
print('Feels like: {}\xb0C'.format(f2c(data['currently']['apparentTemperature'])))
