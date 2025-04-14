class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        """
        >>> s = Stack()
        >>> s.is_empty()
        True
        """
        return len(self.stack) == 0

    def push(self, x: int):
        """
        >>> s = Stack()
        >>> s.push(4)
        >>> s.stack
        [4]
        """
        self.stack.append(x)

    def pop(self) -> int | None:
        if not self.is_empty():
            return self.stack.pop()

        return None

    def top(self) -> int | None:
        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self) -> int:
        return len(self.stack)


class MyQueue:

    def __init__(self):
        self.in_ = Stack()
        self.out_ = Stack()

        self.in_.push(1)

    def push(self, x: int) -> None:
        self.in_.push(x)

    def pop(self) -> int:
        if self.out_.is_empty():
            while not self.in_.is_empty():
                self.out_.push(self.in_.pop())

        return self.out_.pop()

    def peek(self) -> int:
        if self.out_.is_empty():
            while not self.in_.is_empty():
                self.out_.push(self.in_.pop())

        return self.out_.top()

    def empty(self) -> bool:
        return (
            self.in_.is_empty()
            and self.out_.is_empty()
        )
