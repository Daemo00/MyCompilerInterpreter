"""Simple function."""
from .compiler import Compiler
from .parser import Parser
from .tokenizer import Tokenizer


def execute(code):
    """Execute `code`."""
    print(code)
    tokens = Tokenizer(code)
    parser = Parser(list(tokens))
    ast = parser.parse()
    compiler = Compiler(ast)
    bytecode = compiler.compile()
    for byte in bytecode:
        print(byte)
    return bytecode
