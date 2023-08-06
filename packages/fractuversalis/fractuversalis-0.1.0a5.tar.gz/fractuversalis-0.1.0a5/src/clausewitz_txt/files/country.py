from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Dict, List, Tuple, Union


@dataclass
class CountryFile:

    graphical_culture: bytes = b'westerngfx'
    color: Tuple[int, int, int] = (0, 0, 0)
    revolutionary_colors: Tuple[int, int, int] = (0, 0, 0)
    historical_score: int = 0
    historical_council: bytes = b''
    preferred_religion: bytes = b''
    historical_idea_groups: List[bytes] = field(default_factory=list)
    historical_units: List[bytes] = field(default_factory=list)
    monarch_names: List[Tuple[bytes, int]] = field(default_factory=list)
    leader_names: List[bytes] = field(default_factory=list)
    ship_names: List[bytes] = field(default_factory=list)
    army_names: List[bytes] = field(default_factory=list)
    fleet_names: List[bytes] = field(default_factory=list)

    @staticmethod
    def __probe_and_init(txt: Dict[Union[bytes, date], Union[List[any], any]], field_name: bytes, callable: Callable[[any], any]):
        if field_name in txt:
            return callable(txt[field_name])
        return None

    @staticmethod
    def __probe_and_mapify(txt: Dict[Union[bytes, date], Union[List[any], any]], field_name: bytes, prop: Union[any, None], callable: Callable[[any], any]):
        if prop is not None:
            txt[field_name] = callable(prop)

    @classmethod
    def from_serialized_txt(cls, txt: Dict[Union[bytes, date], Union[List[any], any]]) -> 'CountryFile':
        return cls(
            graphical_culture=cls.__probe_and_init(txt, b'graphical_culture', lambda gfx: gfx),
            color=cls.__probe_and_init(txt, b'color', lambda color_list: (color_list[0], color_list[1], color_list[2])),
            revolutionary_colors=cls.__probe_and_init(txt, b'revolutionary_colors', lambda color_list: (color_list[0], color_list[1], color_list[2])),
            historical_score=cls.__probe_and_init(txt, b'historical_score', lambda score: score),
            historical_council=cls.__probe_and_init(txt, b'historical_council', lambda council: council),
            preferred_religion=cls.__probe_and_init(txt, b'preferred_religion', lambda religion: religion),
            historical_idea_groups=cls.__probe_and_init(txt, b'historical_idea_groups', lambda idea_groups: idea_groups),
            historical_units=cls.__probe_and_init(txt, b'historical_units', lambda units: units),
            monarch_names=cls.__probe_and_init(txt, b'monarch_names', lambda names_dict: list(names_dict.items())),
            leader_names=cls.__probe_and_init(txt, b'leader_names', lambda names: names),
            ship_names=cls.__probe_and_init(txt, b'ship_names', lambda names: names),
            army_names=cls.__probe_and_init(txt, b'army_names', lambda names: names),
            fleet_names=cls.__probe_and_init(txt, b'fleet_names', lambda names: names)
        )

    def to_serialized_txt(self) -> Dict[bytes, Union[List[int], List[bytes], Dict[bytes, int], bytes, int]]:
        fields: Dict[bytes, Union[List[int], List[bytes], Dict[bytes, int], bytes, int]] = {}
        self.__probe_and_mapify(fields, b'graphical_culture', self.graphical_culture, lambda gfx: gfx)
        self.__probe_and_mapify(fields, b'color', self.color, lambda color_tuple: list(color_tuple))
        self.__probe_and_mapify(fields, b'revolutionary_colors', self.revolutionary_colors, lambda color_tuple: list(color_tuple))
        self.__probe_and_mapify(fields, b'historical_score', self.historical_score, lambda score: score)
        self.__probe_and_mapify(fields, b'historical_council', self.historical_council, lambda council: council)
        self.__probe_and_mapify(fields, b'preferred_religion', self.preferred_religion, lambda religion: religion)
        self.__probe_and_mapify(fields, b'historical_idea_groups', self.historical_idea_groups, lambda idea_groups: idea_groups)
        self.__probe_and_mapify(fields, b'historical_units', self.historical_units, lambda units: units)
        self.__probe_and_mapify(fields, b'monarch_names', self.monarch_names, lambda names_list: dict(names_list))
        self.__probe_and_mapify(fields, b'leader_names', self.leader_names, lambda names: names)
        self.__probe_and_mapify(fields, b'ship_names', self.ship_names, lambda names: names)
        self.__probe_and_mapify(fields, b'army_names', self.army_names, lambda names: names)
        self.__probe_and_mapify(fields, b'fleet_names', self.fleet_names, lambda names: names)
        return fields
