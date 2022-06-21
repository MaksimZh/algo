class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    pass

class LinkedList2:  
    def __init__(self):
        self.head = DummyNode(None)
        self.tail = DummyNode(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while type(node) is not DummyNode:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head.next
        while type(node) is not DummyNode:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        last = self.head
        node = self.head.next
        flag = True
        while (type(node) is not DummyNode) and flag:
            if node.value == val:
                last.next = node.next
                node.next.prev = last
                flag = all
            else:
                last = node
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        count = 0
        node = self.head.next
        while type(node) is not DummyNode:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            afterNode = self.tail.prev
        newNode.next = afterNode.next
        afterNode.next.prev = newNode
        afterNode.next = newNode
        newNode.prev = afterNode

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head
