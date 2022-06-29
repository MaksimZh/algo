class Stack:
    def __init__(self):
        self.top = LastNode(None)
        self.top.next = self.top

    def size(self):
        count = 0
        node = self.top
        while type(node) is not LastNode:
            node = node.next
            count += 1
        return count

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def peek(self):
        return self.top.value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LastNode(Node):
    pass
