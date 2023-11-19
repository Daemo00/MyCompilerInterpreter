"""Compile the AST to Bytecode."""
from dataclasses import dataclass
from enum import auto, StrEnum
from typing import Any, Generator

from MyCompilerInterpreter.parser import BinOp


class BytecodeType(StrEnum):
    """Type of Bytecode."""

    BINOP = auto()
    PUSH = auto()


@dataclass
class Bytecode:
    """Bytecode."""

    type: BytecodeType
    value: Any = None


class Compiler:
    """Compile the AST to Bytecode."""

    def __init__(self, tree: BinOp) -> None:
        """Create the Compiler."""
        self.tree = tree

    def compile(self) -> Generator[Bytecode, None, None]:
        """Compiler."""
        left = self.tree.left
        yield Bytecode(BytecodeType.PUSH, left.value)

        right = self.tree.right
        yield Bytecode(BytecodeType.PUSH, right.value)

        yield Bytecode(BytecodeType.BINOP, self.tree.op)
