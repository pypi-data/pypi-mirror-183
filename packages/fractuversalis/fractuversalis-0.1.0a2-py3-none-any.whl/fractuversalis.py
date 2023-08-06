"""Shattered world mod generator for EU4"""

__version__ = "0.1.0-alpha.2"


import logging
import clausewitz_txt
from test_files import history_test_file, cultures_test_file, country_test_file


def __try_parsing(s: str):
    try:
        print(clausewitz_txt.loads(s))
    except Exception as e:
        logging.error(str(e))


def main():
    # logging.basicConfig(level=logging.DEBUG)
    __try_parsing(history_test_file)
    __try_parsing(cultures_test_file)
    __try_parsing(country_test_file)


if __name__ == '__main__':
    main()
