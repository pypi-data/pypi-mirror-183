"""Shattered world mod generator for EU4"""

__version__ = "0.1.0-alpha.5"


import logging
import clausewitz_txt
from clausewitz_txt.files.history import HistoryFile
from clausewitz_txt.files.country import CountryFile
from clausewitz_txt.files.cultures import CulturesFile
from test_files import history_test_file, cultures_test_file, country_test_file


def __try_parsing(s: str):
    try:
        return clausewitz_txt.loads(s)
    except Exception as e:
        logging.error(str(e))


def main():
    # logging.basicConfig(level=logging.DEBUG)
    a = __try_parsing(history_test_file)
    fa = HistoryFile.from_serialized_txt(a)
    print(fa)
    print(fa.to_serialized_txt())
    for epoch in fa.epochs():
        print(epoch)
    for cores in fa.field_changes(b'add_core'):
        print(cores)
    for controllers in fa.field_changes(b'controller'):
        print(controllers)

    b = __try_parsing(country_test_file)
    fb = CountryFile.from_serialized_txt(b)
    print(fb)
    print(fb.to_serialized_txt())

    c = __try_parsing(cultures_test_file)
    fc = CulturesFile.from_serialized_txt(c)
    print(fc)
    print(fc.to_serialized_txt())


if __name__ == '__main__':
    main()
