"""Transform code string int a sequence of tokens."""
from dataclasses import dataclass
from enum import StrEnum, auto
from string import digits
from typing import Any, Generator


class TokenType(StrEnum):
    """Token types."""

    INT = auto()
    PLUS = auto()
    MINUS = auto()
    EOF = auto()


@dataclass
class Token:
    """Token."""

    type: TokenType
    value: Any = None


class Tokenizer:
    """Extract tokens from a string."""

    def __init__(self, code: str) -> None:
        """Store `code`."""
        self.code = code
        self.ptr: int = 0

    def next_token(self) -> Token:
        """Get next token."""
        while self.ptr < len(self.code) and self.code[self.ptr] == " ":
            self.ptr += 1

        if self.ptr == len(self.code):
            return Token(TokenType.EOF)

        char = self.code[self.ptr]
        self.ptr += 1
        if char == "+":
            return Token(TokenType.PLUS)
        elif char == "-":
            return Token(TokenType.MINUS)
        elif char in digits:
            return Token(TokenType.INT, int(char))
        else:
            raise RuntimeError(f"Can't tokenize {char!r}.")

    def __iter__(self) -> Generator[Token, None, None]:
        """Iterate over tokens."""
        while (token := self.next_token()).type != TokenType.EOF:
            yield token
        yield token  # Yield the EOF token too.
