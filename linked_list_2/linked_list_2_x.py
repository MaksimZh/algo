class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    pass

class LinkedList2:  
    def __init__(self):
        self.dummy = DummyNode(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def add_in_tail(self, item):
        self.dummy.prev.next = item
        item.prev = self.dummy.prev
        item.next = self.dummy
        self.dummy.prev = item

    def find(self, val):
        node = self.dummy.next
        while type(node) is not DummyNode:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.dummy.next
        while type(node) is not DummyNode:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        last = self.dummy
        node = last.next
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
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def len(self):
        count = 0
        node = self.dummy.next
        while type(node) is not DummyNode:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            afterNode = self.dummy.prev
        newNode.next = afterNode.next
        afterNode.next.prev = newNode
        afterNode.next = newNode
        newNode.prev = afterNode

    def add_in_head(self, newNode):
        newNode.next = self.dummy.next
        self.dummy.next.prev = newNode
        self.dummy.next = newNode
        newNode.prev = self.dummy
