import requests
from urllib.parse import quote
from settings import config


def geocode(location):
    try:
        url = config['location-url'].format(loc=location)
        enc_url = url.format(quote(location))
        res = requests.get(enc_url).json()
        if res['status'] == 'ZERO_RESULTS':
            print('Address not found')
        else:
            return res['results'][0]

    except Exception:
        print('Unable to connect to server')


def weather(latitude, longitude):
    url = config['weather-url'].format(
        key=config['weather-key'],
        lat=latitude,
        lng=longitude
    )

    return requests.get(url).json()


def celcius(f):
    return int((f - 32) * 5 / 9)


def main():
    geo = geocode('90210')
    if not geo:
        return

    lat = geo['geometry']['location']['lat']
    lng = geo['geometry']['location']['lng']

    data = weather(lat, lng)

    print('Address:', geo['formatted_address'])
    print('Weather:', data['currently']['summary'])
    print('Temperature: {}\xb0C'.format(celcius(data['currently']['temperature'])))


if __name__ == '__main__':
    main()
