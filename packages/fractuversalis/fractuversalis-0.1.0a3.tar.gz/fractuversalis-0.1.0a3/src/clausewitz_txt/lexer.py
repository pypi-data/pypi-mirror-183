from dataclasses import dataclass
import io
from enum import Enum, auto
import logging
import re


class LexerTokenType(Enum):
    IGNORE = auto()
    BOOL = auto()
    INT = auto()
    FLOAT = auto()
    DATE = auto()
    PLAIN_STRING = auto()
    STRING = auto()
    EQ = auto()
    BRACE_OPEN = auto()
    BRACE_CLOSE = auto()
    UNKNOWN = auto()


@dataclass
class LexerToken:
    tp: LexerTokenType = LexerTokenType.UNKNOWN
    lexeme: bytes = b''

    def __eq__(self, token_type: LexerTokenType):
        return self.tp == token_type
    
    def __str__(self) -> str:
        return f'{{type: {self.tp.name}, lexeme: {self.lexeme.decode("windows-1252")!r}}}'


class Lexer:

    __regexp_to_tokens = [
        (rb'#.*?\n', LexerTokenType.IGNORE),
        (rb'[ \t\r\n]+', LexerTokenType.IGNORE),
        (rb'=', LexerTokenType.EQ),
        (rb'\{', LexerTokenType.BRACE_OPEN),
        (rb'\}', LexerTokenType.BRACE_CLOSE),
        (rb'(yes|no)(?!\w)', LexerTokenType.BOOL),
        (rb'\d{1,4}\.(1[0-2]|0?[1-9])\.([1-2][0-9]|3[0-1]|0?[1-9])', LexerTokenType.DATE),
        (rb'-?\d+\.\d+', LexerTokenType.FLOAT),
        (rb'-?\d+', LexerTokenType.INT),
        (rb'".*"', LexerTokenType.STRING),
        (rb'\S+', LexerTokenType.PLAIN_STRING)
    ]

    def __init__(self, b: bytes) -> None:
        self.input_stream = b

    @classmethod
    def from_str(cls, s: str) -> 'Lexer':
        return cls(bytes(s, encoding='utf-8'))

    @classmethod
    def from_io(cls, io_stream: io.RawIOBase) -> 'Lexer':
        return cls(io_stream.readall())

    @classmethod
    def from_bufio(cls, io_stream: io.BufferedIOBase) -> 'Lexer':
        return cls(io_stream.raw.readall())

    def __get_next_token(self) -> LexerToken | None:
        if len(self.input_stream) == 0:
            return None
        for regexp, token_type in self.__regexp_to_tokens:
            m = re.match(regexp, self.input_stream)
            if m is not None:
                lexeme = m.group(0)
                self.input_stream = self.input_stream[len(lexeme):]
                return LexerToken(token_type, lexeme)

    def get_token(self) -> LexerToken | None:
        while True:
            tkn = self.__get_next_token()
            if tkn != LexerTokenType.IGNORE:
                logging.debug(f'txt_lexer:return_token:{tkn}')
                return tkn

    def __iter__(self):
        return self

    def __next__(self):
        t = self.get_token()
        if t is None:
            raise StopIteration
        return t
