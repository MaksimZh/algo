class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    pass

class OrderedList:
    def __init__(self, asc):
        self.head = DummyNode(None)
        self.tail = DummyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        node = self.head.next
        compareContinue = 1 if self.__ascending else -1
        while type(node) is not DummyNode:
            if self.compare(value, node.value) != compareContinue:
                break
            node = node.next
        newNode = Node(value)
        newNode.prev = node.prev
        newNode.next = node
        newNode.prev.next = newNode
        newNode.next.prev = newNode

    def find(self, val):
        node = self.head.next
        compareContinue = 1 if self.__ascending else -1
        while type(node) is not DummyNode:
            cmp = self.compare(val, node.value)
            if cmp == 0:
                return node
            elif cmp != compareContinue:
                break
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def clean(self, asc):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.__ascending = asc

    def len(self):
        count = 0
        node = self.head.next
        while type(node) is not DummyNode:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head.next
        while type(node) is not DummyNode:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0
