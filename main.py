import display
import parse

from config import Config
from location import Location
from weather import Weather


def main(args, config):
    address = parse.read(args, config)
    if (address):
        location = Location(address, config)
        if (location.address):
            weather = Weather(location, config)
            display.show(location, weather)


if __name__ == '__main__':
    config = Config()
    args = parse.set()
    if config.api_key:
        main(args, config)
    else:
        if args.key:
            print("main: Save api key")
            config.save(args.address[0])
            # main(args)
        else:
            print("API key no where to be found, run again with --key apikey")
