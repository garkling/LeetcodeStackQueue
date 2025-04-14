class Queue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        """
        >>> q = Queue()
        >>> q.push(1)
        >>> q.queue
        [1]
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        >>> q = Queue()
        >>> q.push(1)
        >>> q.push(2)
        >>> q.pop()
        1
        >>> q.queue
        [2]
        """
        if not self.empty():
            return self.queue.pop(0)

    def peek(self) -> int:
        """
        >>> q = Queue()
        >>> q.push(1)
        >>> q.peek(2)
        >>> q.peek()
        1
        """
        if not self.empty():
            return self.queue[0]

    def empty(self) -> bool:
        """
        >>> q = Queue()
        >>> q.push(1)
        >>> q.empty()
        False
        >>> x = q.pop()
        >>> q.empty()
        True
        """
        return self.size() == 0

    def size(self) -> int:
        return len(self.queue)


class MyStack:

    def __init__(self):
        self.stack_1 = Queue()
        self.stack_2 = Queue()

    def push(self, x: int) -> None:
        self.stack_1.push(x)

    def pop(self) -> int:
        while self.stack_1.size() > 1:
            self.stack_2.push(self.stack_1.pop())

        item = self.stack_1.pop()
        self.stack_1, self.stack_2 = self.stack_2, self.stack_1

        return item

    def top(self) -> int:
        """
        >>> s = MyStack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.top()
        2
        >>> s.push(3)
        >>> s.top()
        3
        """
        while self.stack_1.size() > 1:
            self.stack_2.push(self.stack_1.pop())

        item = self.stack_1.pop()
        self.stack_2.push(item)

        self.stack_1, self.stack_2 = self.stack_2, self.stack_1

        return item

    def empty(self) -> bool:
        return (
            self.stack_1.empty()
            and self.stack_2.empty()
        )
