from datetime import date
from typing import Dict, List, Tuple, Union
from sortedcontainers import SortedDict
from clausewitz_txt import field_properties
from copy import copy


class HistoryFile(SortedDict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_serialized_txt(cls, txt: Dict[Union[bytes, date], Union[List[any], any]], *args, **kwargs) -> 'HistoryFile':
        fl = cls(*args, **kwargs)
        for key, value in txt.items():
            if type(key) is date:
                fl[key] = value
            else:
                fl[date.fromordinal(1)][key] = value
        return fl

    def to_serialized_txt(self) -> Dict[Union[bytes, date], Union[List[any], any]]:
        d = dict(self)
        del d[date.fromordinal(1)]
        for initial_field_key, initial_field_value in self[date.fromordinal(1)].items():
            d[initial_field_key] = initial_field_value
        return d

    def __getitem__(self, key: date) -> Dict[bytes, any]:
        if key not in self:
            self.__setitem__(key, {})
        return super().__getitem__(key)

    def epochs(self) -> Tuple[date, Dict[bytes, any]]:
        actual_values: Dict[bytes, any] = {}
        for dt, values in self.items():
            for key, value in values.items():
                if type(value) is list and key in actual_values and type(actual_values[key]) is list:
                    actual_values[key].extend(value)
                elif key in field_properties.ANTAGONIST_SUBJ:
                    antagonist_key = field_properties.ANTAGONIST_OBJ[field_properties.ANTAGONIST_SUBJ.index(key)]
                    if antagonist_key not in actual_values:
                        continue
                    if type(actual_values[antagonist_key]) is list:
                        actual_values[antagonist_key] = list(filter(lambda val: val not in value, actual_values[antagonist_key]))
                    elif actual_values[antagonist_key] in value:
                        del actual_values[antagonist_key]
                else:
                    actual_values[key] = copy(value)
            yield (dt, actual_values)

    def by_date_of(self, requested_date: date) -> Dict[bytes, any]:
        actual_values: Dict[bytes, any] = {}
        for dt, values in self.epochs():
            if dt > requested_date:
                break
            actual_values = values
        return actual_values

    def __changes_of_dupable_field(self, field: bytes) -> Tuple[date, any]:
        prev_value = []
        for dt, values in self.epochs():
            if field in values and values[field] != prev_value:
                prev_value = copy(values[field])
                yield (dt, prev_value)

    def __changes_of_field(self, field: bytes) -> Tuple[date, any]:
        for dt, values in self.items():
            if field in values:
                yield (dt, values[field])

    def field_changes(self, field: bytes) -> Tuple[date, any]:
        return self.__changes_of_dupable_field(field) \
            if field in field_properties.DUPABLE_FIELDS \
            else self.__changes_of_field(field)
