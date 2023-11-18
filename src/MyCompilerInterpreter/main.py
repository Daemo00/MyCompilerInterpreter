"""Simple function."""
from .tokenizer import Tokenizer, TokenType


def execute(code):
    """Execute `code`."""
    print(code)
    tokenizer = Tokenizer(code)
    while (tok := tokenizer.next_token()).type != TokenType.EOF:
        print(f"\t{tok.type}, {tok.value}")
