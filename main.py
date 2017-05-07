import argparse
import requests
import os.path

from urllib.parse import quote
from settings import config


def url_safe(str):
    str = str.replace(',', ' ').replace('  ', ' ')
    return quote(str)


def fetch_data(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print('Unable to connect to server')
        print(e)


def geocode(location):
    url = config['location-url'].format(loc=url_safe(location))
    data = fetch_data(url)
    if data['status'] == 'ZERO_RESULTS':
        print('Address not found')
    else:
        return data['results'][0]


def weather(latitude, longitude):
    url = config['weather-url'].format(
        key=config['weather-key'],
        lat=latitude,
        lng=longitude
    )
    return fetch_data(url)


def parse_address(address):
    data = ''
    for word in address:
        data += ' ' + word
    return data.strip()


def set_default(location):
    with open(config['save-file'], 'w') as f:
        f.write(str(location))


def get_default():
    if not os.path.exists(config['save-file']):
        return
    with open(config['save-file'], 'r') as f:
        loc = f.read()
    return loc


def set_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("address",
                        help="The address, city or post code for the weather.",
                        nargs='*', type=str)

    parser.add_argument("-l", "--list",
                        help="displays the default location",
                        action="store_true")

    parser.add_argument("-d", "--default",
                        help="saves location as the default and exits",
                        action="store_true")

    parser.add_argument("-s", "--save",
                        help="saves location as the default and fetches weather",
                        action="store_true")

    return parser.parse_args()


def show(location, data):
    print()
    print('Location : {}'.format(location['formatted_address']))
    print('Weather  : {}'.format(data['currently']['summary']))
    print('Currently: {}\xb0C'.format(int(data['currently']['temperature'])))
    print('Forecast : {}'.format(data['daily']['summary']))


def main():

    args = set_parse()

    if args.list:
        print('Default location: {}'.format(get_default()))
        return

    if args.address:
        address = parse_address(args.address)
    else:
        address = get_default()
    if not address:
        print("No default location set.\nPlease run again and include a location.")
        return

    geo = geocode(address)
    if not geo:
        return

    # args that need valid data
    if args.default:
        if args.address:
            set_default(geo['formatted_address'])
            print('Setting {} as default location'.format(geo['formatted_address']))
        else:
            print('No location specified')
        return

    if args.save:
        if args.address:
            set_default(geo['formatted_address'])
            print('Saving {} as default location'.format(geo['formatted_address']))
        else:
            print('No location specified')
            return

    data = weather(geo['geometry']['location']['lat'],
                   geo['geometry']['location']['lng'])

    show(geo, data)

if __name__ == '__main__':
    main()
