"""Simple function."""
from .compiler import Compiler
from .interpreter import Interpreter
from .parser import Parser
from .tokenizer import Tokenizer


def execute(code):
    """Execute `code`."""
    tokens = Tokenizer(code)

    parser = Parser(list(tokens))
    ast = parser.parse()

    compiler = Compiler(ast)
    bytecode = compiler.compile()

    interpreter = Interpreter(list(bytecode))
    interpreter.interpret()
