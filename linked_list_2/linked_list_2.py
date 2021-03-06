class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        if all:
            nodes = self.find_all(val)
        else:
            nodes = [self.find(val)]
        if nodes == [] or nodes == [None]:
            return
        for node in nodes:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            elif node is self.head:
                self.head = node.next
                self.head.prev = None
                node.next = None
            elif node is self.tail:
                self.tail = node.prev
                self.tail.next = None
                node.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
                node.next = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if (afterNode is None) or (afterNode is self.tail):
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode
            newNode.prev = afterNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
