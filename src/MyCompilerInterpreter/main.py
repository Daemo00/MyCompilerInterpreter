"""Simple function."""
from .tokenizer import Tokenizer


def execute(code):
    """Execute `code`."""
    print(code)
    tokenizer = Tokenizer(code)
    for tok in tokenizer:
        print(f"\t{tok.type}, {tok.value}")
