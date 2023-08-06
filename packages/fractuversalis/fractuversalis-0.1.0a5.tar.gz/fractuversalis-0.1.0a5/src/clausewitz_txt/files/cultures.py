from dataclasses import dataclass, field
from typing import Dict, List, Union
from copy import copy


@dataclass
class CultureProperties:
    primary: bytes = b''
    graphical_culture: bytes = b''
    country: Dict[bytes, any] = field(default_factory=dict)
    province: Dict[bytes, any] = field(default_factory=dict)
    male_names: List[bytes] = field(default_factory=list)
    female_names: List[bytes] = field(default_factory=list)
    dynasty_names: List[bytes] = field(default_factory=list)

    def set_or_extend(self, field_name: bytes, value: any):
        if field_name == b'primary':
            self.primary = value
        elif field_name == b'graphical_culture':
            self.graphical_culture = value
        elif field_name == b'country':
            self.country = {**self.country, **value}
        elif field_name == b'province':
            self.province = {**self.province, **value}
        elif field_name == b'male_names':
            self.male_names.extend(value)
        elif field_name == b'female_names':
            self.female_names.extend(value)
        elif field_name == b'dynasty_names':
            self.dynasty_names.extend(value)

    @classmethod
    def merge(cls, subj: 'CultureProperties', obj: 'CultureProperties') -> 'CultureProperties':
        new_props = cls()
        new_props.primary = obj.primary if len(obj.primary) != 0 else subj.primary
        new_props.graphical_culture = obj.graphical_culture if len(obj.graphical_culture) != 0 else subj.graphical_culture
        new_props.country = {**subj.country, **obj.country}
        new_props.province = {**subj.province, **obj.province}
        new_props.male_names = [*subj.male_names, *obj.male_names]
        new_props.female_names = [*subj.female_names, *obj.female_names]
        new_props.dynasty_names = [*subj.dynasty_names, *obj.dynasty_names]
        return new_props

    @classmethod
    def from_serialized_txt(cls, txt: Dict[bytes, any]):
        props = cls()
        if b'primary' in txt:
            props.primary = txt[b'primary']
        if b'graphical_culture' in txt:
            props.graphical_culture = txt[b'graphical_culture']
        if b'country' in txt:
            props.country = copy(txt[b'country'])
        if b'province' in txt:
            props.province = copy(txt[b'province'])
        if b'male_names' in txt:
            props.male_names = copy(txt[b'male_names'])
        if b'female_names' in txt:
            props.female_names = copy(txt[b'female_names'])
        if b'dynasty_names' in txt:
            props.dynasty_names = copy(txt[b'dynasty_names'])
        return props

    def to_serialized_txt(self) -> Dict[bytes, Union[bytes, List[bytes], Dict[bytes, any]]]:
        txt: Dict[bytes, Union[bytes, List[bytes], Dict[bytes, any]]] = dict()
        if len(self.primary) != 0:
            txt[b'primary'] = self.primary
        if len(self.graphical_culture) != 0:
            txt[b'graphical_culture'] = self.graphical_culture
        if len(self.country) != 0:
            txt[b'country'] = self.country
        if len(self.province) != 0:
            txt[b'province'] = self.province
        if len(self.male_names) != 0:
            txt[b'male_names'] = self.male_names
        if len(self.female_names) != 0:
            txt[b'female_names'] = self.female_names
        if len(self.dynasty_names) != 0:
            txt[b'dynasty_names'] = self.dynasty_names
        return txt


@dataclass
class CulturesFile:
    cultures: Dict[bytes, CultureProperties] = field(default_factory=dict)
    culture_groups: Dict[bytes, List[bytes]] = field(default_factory=dict)

    @classmethod
    def from_serialized_txt(cls, txt: Dict[bytes, Union[any, Dict[bytes, any]]]) -> 'CulturesFile':
        fl = cls()
        for culture_group, cultures_and_props in txt.items():
            culture_group_scope_props = CultureProperties()
            for prop_name, prop_value in cultures_and_props.items():
                if prop_name not in (b'primary', b'graphical_culture', b'country', b'province', b'male_names', b'female_names', b'dynasty_names'):
                    continue
                culture_group_scope_props.set_or_extend(prop_name, prop_value)
            for culture_name, culture_value in cultures_and_props.items():
                if culture_name in (b'primary', b'graphical_culture', b'country', b'province', b'male_names', b'female_names', b'dynasty_names')\
                  or type(culture_value) is not dict:
                    continue
                if culture_group not in fl.culture_groups:
                    fl.culture_groups[culture_group] = list()
                fl.culture_groups[culture_group].append(culture_name)
                fl.cultures[culture_name] = CultureProperties.merge(culture_group_scope_props, CultureProperties.from_serialized_txt(culture_value))
        return fl

    def to_serialized_txt(self) -> Dict[bytes, Dict[bytes, Dict[bytes, Union[bytes, List[bytes], Dict[bytes, any]]]]]:
        txt: Dict[bytes, Dict[bytes, Dict[bytes, Union[bytes, List[bytes], Dict[bytes, any]]]]] = {}
        for culture_group, cultures in self.culture_groups.items():
            cultures_txt: Dict[bytes, Dict[bytes, Union[bytes, List[bytes], Dict[bytes, any]]]] = {}
            for culture_name in cultures:
                cultures_txt[culture_name] = self.cultures[culture_name].to_serialized_txt()
            txt[culture_group] = cultures_txt
        return txt
