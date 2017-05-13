import display
import parse

from config import Config
from location import Location
from weather import Weather


def main():
    args = parse.set()
    config = Config()

    address = parse.read(args, config)

    if not config.api_key:
        if not config.api_key:
            print("API key not found, run again with --key apikey")
            return

    if (address):
        location = Location(address, config.location_url)
        if (location.address):
            weather = Weather(location, config)
            display.show(location, weather)
        return

    if not args.key:
        print('No address supplied')


if __name__ == '__main__':
    main()
