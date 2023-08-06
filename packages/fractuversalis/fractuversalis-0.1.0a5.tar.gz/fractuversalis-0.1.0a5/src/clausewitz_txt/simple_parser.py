from datetime import date
from typing import Dict, List, Union
from .lexer import LexerToken, LexerTokenType, Lexer
from clausewitz_txt import field_properties


class Parser:

    def __init__(self, lexer: Lexer) -> None:
        self.__lexer = lexer

    @classmethod
    def __dict_append(cls, d: Dict[Union[bytes, date], Union[List[any], any]], key: str, value: any):
        if type(value) is dict:
            if key not in d:
                d[key] = value
            else:
                d[key] = {**d[key], **value}
        elif key in field_properties.DUPABLE_FIELDS:
            if key not in d:
                d[key] = [value]
            else:
                d[key].append(value)
        else:
            d[key] = value

    def __parse_value(self, val: LexerToken):
        if val == LexerTokenType.BOOL:
            return val.lexeme in ['yes', 'true']
        elif val == LexerTokenType.INT:
            return int(val.lexeme)
        elif val == LexerTokenType.FLOAT:
            return float(val.lexeme)
        elif val == LexerTokenType.PLAIN_STRING:
            return val.lexeme
        elif val == LexerTokenType.STRING:
            return val.lexeme[1:-1]
        elif val == LexerTokenType.BRACE_OPEN:
            return self.parse_object()

    def __parse_list(self, *args: LexerToken):
        arglist = list(args)
        value = LexerToken()
        while True:
            value = self.__lexer.get_token()
            if value in (LexerTokenType.BOOL, LexerTokenType.INT, LexerTokenType.FLOAT,
                         LexerTokenType.PLAIN_STRING, LexerTokenType.STRING):
                arglist.append(value)
            else:
                break
        if value != LexerTokenType.BRACE_CLOSE:
            raise Exception(f'unknown element {value} terminated the list')
        return [self.__parse_value(token) for token in arglist]

    def parse_object(self) -> Dict[Union[bytes, date], Union[List[any], any]]:
        d: Dict[Union[bytes, date], Union[List[any], any]] = {}
        while True:
            key = self.__lexer.get_token()
            if key in (LexerTokenType.BOOL, LexerTokenType.INT, LexerTokenType.FLOAT):
                return self.__parse_list(key)
            if key in (LexerTokenType.PLAIN_STRING, LexerTokenType.STRING):
                eq = self.__lexer.get_token()
                if eq == LexerTokenType.EQ:  # Keypair: key = value
                    val = self.__lexer.get_token()
                    self.__dict_append(d, self.__parse_value(key), self.__parse_value(val))
                elif eq in (LexerTokenType.PLAIN_STRING, LexerTokenType.STRING):  # List: val1 val2 ...
                    return self.__parse_list(key, eq)
                elif eq == LexerTokenType.BRACE_CLOSE:  # 1-element list: val
                    return [self.__parse_value(key)]
                else:
                    raise Exception(f'the object is neither a map nor a list! first two elements are {key} {eq}')
            elif key == LexerTokenType.DATE:
                _, val = self.__lexer.get_token(), self.__lexer.get_token()
                year, month, day = key.lexeme.split(b'.', maxsplit=2)
                self.__dict_append(d, date(int(year), int(month), int(day)), self.__parse_value(val))
            elif key == LexerTokenType.BRACE_CLOSE or key is None:
                return d
            else:
                raise Exception(f'the object is neither a map nor a list! the first element is {key}')
