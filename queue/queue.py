class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def enqueue(self, item):
        node = Node(item)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self._size += 1

    def dequeue(self):
        node = self.head.next
        if self._size > 0:
            self.head.next = node.next
            node.next.prev = self.head
            self._size -= 1
        return node.value

    def size(self):
        return self._size


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
