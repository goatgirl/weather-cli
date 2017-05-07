import argparse
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


def parse_address(address):
    data = ''
    for word in address:
        data += ' ' + word
    return data.strip()


def set_default(location):
    with open("weather.sav", 'w') as f:
        f.write(str(location))


def get_default():
    with open("weather.sav", 'r') as f:
        loc = f.read()
    return loc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("address",
                        help="The address, city or post code for the weather.",
                        nargs='*', type=str)

    parser.add_argument("-d", "--default",
                        help="Sets the  location as the default location and exits",
                        action="store_true")

    parser.add_argument("-s", "--set",
                        help="Sets the  location as the default location and fetches weather",
                        action="store_true")

    args = parser.parse_args()

    if args.address:
        address = parse_address(args.address)
    else:
        address = get_default()

    if not address:
        print("No default location set.\nPlease run again and include an address.")
        return

    geo = geocode(address)
    if not geo:
        return

    if args.default:
        set_default(geo['formatted_address'])
        print('Setting {} as default location'.format(geo['formatted_address']))
        return

    if args.set:
        set_default(geo['formatted_address'])
        print('Setting {} as default location'.format(geo['formatted_address']))

    lat = geo['geometry']['location']['lat']
    lng = geo['geometry']['location']['lng']

    data = weather(lat, lng)

    print()
    print('Location :', geo['formatted_address'])
    print('Weather  :', data['currently']['summary'])
    print('Currently: {}\xb0C'.format(int(data['currently']['temperature'])))
    print('Forecast :', data['daily']['summary'])


if __name__ == '__main__':
    main()
