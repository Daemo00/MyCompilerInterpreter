"""Test the interpreter."""
from MyCompilerInterpreter.tokenizer import Tokenizer
from MyCompilerInterpreter.parser import Parser
from MyCompilerInterpreter.compiler import Compiler
from MyCompilerInterpreter.interpreter import Interpreter

import pytest


@pytest.mark.parametrize(
    ["code", "result"],
    [
        ("3 + 5", 8),
        ("5 - 2", 3),
        ("1 + 2", 3),
        ("1 - 9", -8),
    ],
)
def test_simple_arithmetic(code: str, result: int):
    """Test  simple operations."""
    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    interpreter = Interpreter(bytecode)
    interpreter.interpret()
    assert interpreter.stack.pop() == result
