from location import Location
from weather import Weather
import display
import parse


def main():
    args = parse.set()
    address = parse.read(args)
    if (address):
        location = Location(address)
        if (location.address):
            weather = Weather(location)
            display.show(location, weather)


if __name__ == '__main__':
    main()
