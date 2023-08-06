from datetime import date
import re


__indent_step = 4
__line_limit_length = 120
__dupable_params = [b'add_core', b'remove_core', b'add_to_trade_company', b'discovered_by',
                    b'add_accepted_culture', b'remove_accepted_culture',
                    b'historical_friend', b'historical_rival',
                    b'add_army_professionalism']


def __nl(indent: int = 0) -> bytes:
    return b'\n' + b' ' * indent


def __deserialize(struct: any, indent: int = 0) -> bytes:
    if type(struct) is bytes:
        if re.search(rb"\s", struct) is not None:
            return b'"' + struct + b'"'
        return struct
    elif type(struct) is date:
        return b'%d' % struct.year + b'.' + b'%d' % struct.month + b'.' + b'%d' % struct.day
    elif type(struct) is int:
        return b'%d' % struct
    elif type(struct) is float:
        return b'%f' % struct
    elif type(struct) is bool:
        return b'yes' if struct == True else b'no'

    elif type(struct) is dict:
        if len(struct) == 0:
            return b'{}'
        s = b'{' + __nl(indent)
        for key, value in struct.items():
            deserialized_key = __deserialize(key, indent + __indent_step)
            if deserialized_key in __dupable_params and type(value) is list:
                for val in value:
                    s += deserialized_key + b' = ' + __deserialize(val, indent + __indent_step) + __nl(indent)
            else:
                s += deserialized_key + b' = ' + __deserialize(value, indent + __indent_step) + __nl(indent)
        s += b'}'
        return s

    elif type(struct) is list:
        if len(struct) <= 5 \
            or type(struct[0]) is int and len(struct) <= 20 \
            or type(struct[0]) is float and len(struct) <= 10:
                return b'{ ' + b' '.join((__deserialize(val) for val in struct)) + b' }'
        s = b'{' + __nl(indent)
        line_length = indent
        for value in struct:
            if line_length > __line_limit_length:
                s += __nl(indent)
                line_length = indent
            deserialized_value = __deserialize(value, indent + __indent_step)
            s += deserialized_value + b' '
            line_length += len(deserialized_value) + 1
        s += __nl(indent) + b'}'
        return s

    else:
        raise Exception(f'{struct} is of unexpected type for deserializing into clausewitz txt!')


def deserialize_start(struct: any) -> bytes:
    if type(struct) is dict:
        s = b''
        for key, value in struct.items():
            deserialized_key = __deserialize(key, __indent_step)
            if deserialized_key in __dupable_params and type(value) is list:
                for val in value:
                    s += deserialized_key + b' = ' + __deserialize(val, __indent_step) + b'\n'
            else:
                s += deserialized_key + b' = ' + __deserialize(value, __indent_step) + b'\n'
        return s
    return __deserialize(struct)
