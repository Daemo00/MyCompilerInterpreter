"""Execute Bytecode."""
from .compiler import Bytecode, BytecodeType


class Stack:
    """Stack of operations."""

    def __init__(self) -> None:
        """Create the stack."""
        self.stack: list[int] = []

    def push(self, item: int) -> None:
        """Add an operation or value."""
        self.stack.append(item)

    def pop(self) -> int:
        """Extract last operation or value."""
        return self.stack.pop()

    def peek(self) -> int:
        """Look at following operation or value."""
        return self.stack[-1]

    def __repr__(self) -> str:
        """Show what is in the stack."""
        return f"Stack({self.stack})"


class Interpreter:
    """Execute bytecode."""

    def __init__(self, bytecode: list[Bytecode]) -> None:
        """Create the interpreter."""
        self.stack = Stack()
        self.bytecode = bytecode
        self.ptr: int = 0

    def interpret(self) -> None:
        """Execute the bytecode."""
        for bc in self.bytecode:
            # Interpret this bytecode operator.
            if bc.type == BytecodeType.PUSH:
                self.stack.push(bc.value)
            elif bc.type == BytecodeType.BINOP:
                right = self.stack.pop()
                left = self.stack.pop()
                if bc.value == "+":
                    result = left + right
                elif bc.value == "-":
                    result = left - right
                else:
                    raise RuntimeError(f"Unknown operator {bc.value}.")
                self.stack.push(result)

        print("Done!")
        print(self.stack)
