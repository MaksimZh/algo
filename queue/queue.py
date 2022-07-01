class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self._size = 0

    def enqueue(self, item):
        node = Node(item)
        self.tail.next = node
        self.tail = node
        self._size += 1

    def dequeue(self):
        if self._size > 0:
            node = self.head.next
            self.head.next = node.next
            self._size -= 1
            return node.value
        else:
            return None

    def size(self):
        return self._size


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
