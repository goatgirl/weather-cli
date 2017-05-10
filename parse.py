import argparse
import config
import file
from location import Location


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

    if args.list:
        print('Default location: {}'.format(file.read(config.save_file)))
        return

    if args.address:
        location = Location(parse_address(args.address))
        if not location.address:
            print('address not recognised')
            return
        address = location.address
    else:
        address = file.read(config.save_file)
        if not address:
            print("No default location set.")
            print("Please run again and include a location.")
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
