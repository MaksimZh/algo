class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            # list is empty
            self.head = newNode
            self.tail = newNode
            return
        node = self.head
        compareContinue = 1 if self.__ascending else -1
        while node is not None:
            if self.compare(newNode.value, node.value) != compareContinue:
                break
            node = node.next
        if node is None:
            # insert to tail
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        elif node is self.head:
            # insert ot head
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            # insert in middle
            newNode.prev = node.prev
            newNode.next = node
            newNode.prev.next = newNode
            newNode.next.prev = newNode

    def find(self, val):
        node = self.head
        compareContinue = 1 if self.__ascending else -1
        while node is not None:
            cmp = self.compare(val, node.value)
            if cmp == 0:
                return node
            elif cmp != compareContinue:
                break
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = trim(v1)
        v2 = trim(v2)
        for i in range(0, min(len(v1), len(v2))):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        if len(v1) < len(v2):
            return -1
        elif len(v1) == len(v2):
            return 0
        else:
            return 1

def trim(v):
    f = len(v) - 1
    while f >= 0 and v[f] == " ":
        f -= 1
    s = 0
    while s < f and v[s] == " ":
        s += 1
    return v[s : f + 1]
