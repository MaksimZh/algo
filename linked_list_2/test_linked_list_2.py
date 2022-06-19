import unittest

from linked_list_2 import Node, LinkedList2


def fillListTail(l, source):
    for s in source:
        l.add_in_tail(s)


class Test(unittest.TestCase):

    def checkList(self, l, test):
        if not test:
            self.assertIsNone(l.head)
            self.assertIsNone(l.tail)
        else:
            last = None
            node = l.head
            i = 0
            while node is not None:
                self.assertIs(node, test[i])
                self.assertIs(node.prev, last)
                i += 1
                last = node
                node = node.next
            self.assertIs(l.tail, test[-1])

    def test_add(self):
        l = LinkedList2()
        n = [Node(0), Node(1), Node(2), Node(3)]
        self.checkList(l, [])
        l.add_in_tail(n[0])
        self.checkList(l, n[0:1])
        l.add_in_tail(n[1])
        self.checkList(l, n[0:2])
        fillListTail(l, n[2:])
        self.checkList(l, n)


    def test_find(self):
        l = LinkedList2()
        n = [Node(0), Node(1), Node(2), Node(3)]
        self.assertIs(l.find(42), None)
        fillListTail(l, n[0:1])
        self.assertIs(l.find(42), None)
        self.assertIs(l.find(0), n[0])
        fillListTail(l, n[1:])
        self.assertIs(l.find(42), None)
        self.assertIs(l.find(2), n[2])

    def test_find_all(self):
        l = LinkedList2()
        n = [Node(0), Node(1), Node(2), Node(2), Node(1), Node(3)]
        self.assertListEqual(l.find_all(42), [])
        fillListTail(l, n[0:1])
        self.assertListEqual(l.find_all(42), [])
        self.assertListEqual(l.find_all(0), n[0:1])
        fillListTail(l, n[1:])
        self.assertListEqual(l.find_all(42), [])
        self.assertListEqual(l.find_all(0), n[0:1])
        self.assertListEqual(l.find_all(1), [n[1], n[4]])
        self.assertListEqual(l.find_all(2), n[2:4])
        self.assertListEqual(l.find_all(3), n[-1:])

    def test_delete(self):
        l = LinkedList2()
        n = [Node(0), Node(1), Node(2), Node(3), Node(2)]
        fillListTail(l, n)
        l.delete(42)
        self.checkList(l, n)
        l.delete(2)
        self.checkList(l, n[:2] + n[3:])
        l.delete(2)
        self.checkList(l, n[:2] + n[3:4])
        l.delete(0)
        self.checkList(l, [n[1], n[3]])
        l.delete(1)
        self.checkList(l, [n[3]])
        l.delete(1)
        self.checkList(l, [n[3]])
        l.delete(3)
        self.checkList(l, [])
        l.delete(3)
        self.checkList(l, [])

    def test_delete_all(self):
        l = LinkedList2()
        n = [Node(0), Node(0), Node(1), Node(1), Node(4), Node(2), Node(3), Node(3), Node(2)]
        fillListTail(l, n)
        l.delete(42, all=True)
        self.checkList(l, n)
        l.delete(2, all=True)
        self.checkList(l, n[:5] + n[6:8])
        l.delete(1, all=True)
        self.checkList(l, n[:2] + n[4:5] + n[6:8])
        l.delete(0, all=True)
        self.checkList(l, n[4:5] + n[6:8])
        l.delete(3, all=True)
        self.checkList(l, n[4:5])
        l.delete(3, all=True)
        self.checkList(l, n[4:5])
        l.delete(4, all=True)
        self.checkList(l, [])
        l.delete(4, all=True)
        self.checkList(l, [])
        fillListTail(l, n[:2])
        l.delete(0, all=True)
        self.checkList(l, [])

    def test_insert(self):
        l = LinkedList2()
        n = [Node(0), Node(1), Node(2), Node(3)]
        l.insert(None, n[0])
        self.checkList(l, n[0:1])
        l.insert(None, n[1])
        self.checkList(l, n[:2])
        l.insert(n[1], n[3])
        self.checkList(l, n[:2] + n[3:])
        l.insert(n[1], n[2])
        self.checkList(l, n)


if __name__ == '__main__':
    unittest.main()
