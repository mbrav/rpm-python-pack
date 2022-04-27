import argparse
from importlib import metadata

from .url import get_weather


def main():
    parser = argparse.ArgumentParser(
        description="Demo RPM builder for python packages")

    parser.add_argument(
        '--verbose',
        '-v',
        help='increase output verbosity',
        action='store_true')
    parser.add_argument(
        '--quiet',
        '-q',
        help='decrease output verbosity',
        action='store_true')

    parser.add_argument(
        '--weather',
        '-w',
        help='Get weather',
        action='store_true')

    version = metadata.version('python-pack-script')
    print(f'This is python-pack-script v{version}!')

    args = parser.parse_args()
    if args.verbose:
        print("verbosity turned on")
    if args.quiet:
        print("verbosity turned off")
    if args.weather:
        result = get_weather()
        print(result)

if __name__ == '__main__':
    main()
