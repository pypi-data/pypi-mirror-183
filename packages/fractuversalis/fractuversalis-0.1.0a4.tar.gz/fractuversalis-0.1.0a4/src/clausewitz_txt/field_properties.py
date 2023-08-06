from typing import List, Tuple


DUPABLE_FIELDS = [b'add_core', b'remove_core', b'add_to_trade_company', b'discovered_by',
                  b'add_accepted_culture', b'remove_accepted_culture',
                  b'historical_friend', b'historical_rival',
                  b'add_army_professionalism']


__antagonists: List[Tuple[bytes, bytes]] = [
    (b'remove_core', b'add_core'),
    (b'remove_accepted_culture', b'add_accepted_culture')
]
ANTAGONIST_SUBJ: List[bytes] = [antagonist_pair[0] for antagonist_pair in __antagonists]
ANTAGONIST_OBJ: List[bytes] = [antagonist_pair[1] for antagonist_pair in __antagonists]


INVALID_TAGS = ['ADD', 'ADM', 'AND', 'ART', 'AUX',
                'CAR', 'CAT', 'CAV', 'CON', 'DIP',
                'HAS', 'HRE', 'INF', 'MIL', 'MIN',
                'NOT', 'NUL', 'PRN', 'RGB', 'SUM',
                'VAL', 'VAN']
