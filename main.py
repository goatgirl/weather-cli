import display
import parse
import file

from location import Location
from weather import Weather


def main():
    args = parse.set()
    address = parse.read(args)
    if (address):
        location = Location(address)
        if (location.address):
            weather = Weather(location)
            display.show(location, weather)


if __name__ == '__main__':
    if file.exists('settings.py'):
        main()
