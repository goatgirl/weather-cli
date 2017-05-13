import argparse
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


def read(args, config):
    address = None

    if args.list:
        if config.api_key:
            print('Default location: {}'.format(file.read(config.save_file)))
        return

    if args.key:
        if args.address:
            key = [parse_address(args.address)]
            loc = config.default_location
            config.save(key[0], loc)
            print('API key stored')
            return
        if config.api_key:
            print("To change API, use: -k <api-key>")
        return

    if args.address:
        address = parse_address(args.address)
        if not address:
            return
    else:
        if file.exists(config.save_file):
            data = file.read_json(config.save_file)
            if(data):
                address = data['default_location']

    if args.default:
        if args.address:
            key = config.api_key
            loc = address
            config.save(key, loc)
            print('Saving {} as default location'
                  .format(address))
        return

    if args.save:
        if args.address:
            key = config.api_key
            loc = address
            config.save(key, loc)
            print('Saving {} as default location'
                  .format(address))
        else:
            if config.api_key:
                print('No location specified')
            return

    return address
