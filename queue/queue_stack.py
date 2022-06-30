class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        if self.outStack.size() == 0:
            while self.inStack.size() > 0:
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

    def size(self):
        return self.inStack.size() + self.outStack.size()

class Stack:
    def __init__(self):
        self.top = Node(None)
        self._size = 0

    def size(self):
        return self._size

    def pop(self):
        node = self.top
        if self._size > 0:
            self.top = node.next
            self._size -= 1
        return node.value

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self._size += 1

    def peek(self):
        return self.top.value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
