import unittest

from linked_list import Node, LinkedList


class Test(unittest.TestCase):

    def checkList(self, l, test):
        if not test:
            self.assertIsNone(l.head)
            self.assertIsNone(l.tail)
        else:
            self.assertIs(l.tail, test[-1])
            i = 0
            node = l.head
            while node != None:
                self.assertIs(node, test[i])
                node = node.next
                i += 1

    def test_add(self):
        l = LinkedList()
        n1 = Node(12)
        n2 = Node(55)
        self.checkList(l, [])
        l.add_in_tail(n1)
        self.checkList(l, [n1])
        l.add_in_tail(n2)
        self.checkList(l, [n1, n2])

    def test_find(self):
        l = LinkedList()
        self.assertIs(l.find(2), None)
        nodes = [Node(0), Node(1), Node(2), Node(3), Node(2)]
        for node in nodes:
            l.add_in_tail(node)
        self.assertIs(l.find(2), nodes[2])
        self.assertIs(l.find(42), None)

    def test_delete(self):
        l = LinkedList()
        nodes = [Node(0), Node(1), Node(2), Node(3), Node(2)]
        for node in nodes:
            l.add_in_tail(node)
        l.delete(42)
        self.checkList(l, nodes)
        l.delete(2)
        self.checkList(l, nodes[:2] + nodes[3:])
        l.delete(2)
        self.checkList(l, nodes[:2] + nodes[3:4])
        l.delete(0)
        self.checkList(l, [nodes[1], nodes[3]])
        l.delete(1)
        self.checkList(l, [nodes[3]])
        l.delete(1)
        self.checkList(l, [nodes[3]])
        l.delete(3)
        self.checkList(l, [])
        l.delete(3)
        self.checkList(l, [])

    def test_delete_all(self):
        l = LinkedList()
        nodes = [Node(0), Node(0), Node(1), Node(1), Node(4), Node(2), Node(3), Node(3), Node(2)]
        for node in nodes:
            l.add_in_tail(node)
        l.delete(42, all=True)
        self.checkList(l, nodes)
        l.delete(2, all=True)
        self.checkList(l, nodes[:5] + nodes[6:8])
        l.delete(1, all=True)
        self.checkList(l, nodes[:2] + nodes[4:5] + nodes[6:8])
        l.delete(0, all=True)
        self.checkList(l, nodes[4:5] + nodes[6:8])
        l.delete(3, all=True)
        self.checkList(l, nodes[4:5])
        l.delete(3, all=True)
        self.checkList(l, nodes[4:5])
        l.delete(4, all=True)
        self.checkList(l, [])
        l.delete(4, all=True)
        self.checkList(l, [])

    def test_clean(self):
        l = LinkedList()
        l.clean()
        self.checkList(l, [])
        l.add_in_tail(Node(1))
        l.add_in_tail(Node(2))
        l.clean()
        self.checkList(l, [])


if __name__ == '__main__':
    unittest.main()
