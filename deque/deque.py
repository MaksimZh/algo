class Deque:
    def __init__(self):
        self.front = Node(None)
        self.tail = Node(None)
        self.front.next = self.tail
        self.tail.prev = self.front
        self.__size = 0

    def addFront(self, item):
        node = Node(item)
        node.next = self.front.next
        self.front.next = node
        node.next.prev = node
        node.prev = self.front
        self.__size += 1

    def addTail(self, item):
        node = Node(item)
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
        self.__size += 1

    def removeFront(self):
        if self.__size == 0:
            return None
        node = self.front.next
        self.front.next = node.next
        node.next.prev = self.front
        self.__size -= 1
        return node.value

    def removeTail(self):
        if self.__size == 0:
            return None
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.__size -= 1
        return node.value

    def size(self):
        return self.__size


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
