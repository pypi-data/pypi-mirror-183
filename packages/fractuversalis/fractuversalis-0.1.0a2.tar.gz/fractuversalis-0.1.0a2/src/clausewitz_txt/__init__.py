import io
from .lexer import Lexer
from .simple_parser import Parser

def loads(s: str):
    return Parser(Lexer.from_str(s)).parse_object()

def load(fd: io.RawIOBase | io.BufferedIOBase):
    if type(fd) is io.RawIOBase:
        return Parser(Lexer.from_io(fd)).parse_object()
    return Parser(Lexer.from_bufio(fd)).parse_object()
