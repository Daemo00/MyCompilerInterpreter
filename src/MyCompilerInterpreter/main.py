"""Simple function."""
from .parser import Parser
from .tokenizer import Tokenizer


def execute(code):
    """Execute `code`."""
    print(code)
    tokens = Tokenizer(code)
    parser = Parser(list(tokens))
    parser.parse()
