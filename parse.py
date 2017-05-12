import argparse
from config import Config
from location import Location

import file


def parse_address(address):
    data = ''
    for word in address:
        data += ' ' + word
    return data.strip()


def set():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "address",
        help="The address, city or post code for the weather.",
        nargs='*', type=str)

    parser.add_argument(
        "-k", "--key",
        help="saves API key from darksky.net",
        action="store_true")

    parser.add_argument(
        "-l", "--list",
        help="displays the default location",
        action="store_true")

    parser.add_argument(
        "-d", "--default",
        help="saves location as the default and exits",
        action="store_true")

    parser.add_argument(
        "-s", "--save",
        help="save location as the default and fetch weather",
        action="store_true")

    return parser.parse_args()


def read(args):
    config = Config()

    if args.address:
        print(args.address)
        location = Location(parse_address(args.address))
        print(location.address)
        if not location.address:
            return
        address = location.address
    else:
        data = file.read(config.save_file)
        location = Location(data)
        address = location.address

    if args.key:
        print("key", address)
        config.save_config(address)
        return

    if args.list:
        print('Default location: {}'.format(file.read(config.save_file)))
        return

    if args.default:
        if args.address:
            file.save(config.save_file, address)
            print('Saving {} as default location'
                  .format(address))
        else:
            print('No location specified')
        return

    if args.save:
        if args.address:
            file.save(config.save_file, address)
            print('Saving {} as default location'
                  .format(address))
        else:
            print('No location specified')
            return

    return address
