"""Parse tokens to AST."""
from dataclasses import dataclass

from .tokenizer import TokenType, Token


@dataclass
class TreeNode:
    """Node of the AST."""

    pass


@dataclass
class Int(TreeNode):
    """Integer tree node."""

    value: int


@dataclass
class BinOp(TreeNode):
    """Binary operator tree node."""

    op: str
    left: "Int"
    right: "Int"


class Parser:
    """Parse tokens to AST."""

    def __init__(self, tokens: list[Token]) -> None:
        """Create the parser."""
        self.tokens = tokens
        self.next_token_index: int = 0
        """Points to the next token to be consumed."""

    def eat(self, expected_token_type: TokenType) -> Token:
        """Return the next token if it is of the expected type.

        If the next token is not of the expected type, this raises an
        error.
        """
        next_token = self.tokens[self.next_token_index]
        self.next_token_index += 1
        if next_token.type != expected_token_type:
            raise RuntimeError(
                f"Expected {expected_token_type}, ate {next_token!r}.",
            )
        return next_token

    def peek(self, skip: int = 0) -> TokenType | None:
        """Check the type of an upcoming token without consuming it."""
        peek_at = self.next_token_index + skip
        return self.tokens[peek_at].type if peek_at < len(self.tokens) else None

    def parse(self) -> BinOp:
        """Parse the program."""
        left_op = self.eat(TokenType.INT)

        if self.peek() == TokenType.PLUS:
            op = "+"
            self.eat(TokenType.PLUS)
        else:
            op = "-"
            self.eat(TokenType.MINUS)

        right_op = self.eat(TokenType.INT)
        self.eat(TokenType.EOF)
        return BinOp(op, Int(left_op.value), Int(right_op.value))
