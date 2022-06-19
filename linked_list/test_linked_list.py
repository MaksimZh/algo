import unittest

from linked_list import Node, LinkedList


def addToList(dest, src):
    for s in src:
        dest.add_in_tail(s)

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


class Test(unittest.TestCase):

    def test_add(self):
        l = LinkedList()
        n1 = Node(12)
        n2 = Node(55)
        checkList(self, l, [])
        l.add_in_tail(n1)
        checkList(self, l, [n1])
        l.add_in_tail(n2)
        checkList(self, l, [n1, n2])

    def test_find(self):
        l = LinkedList()
        self.assertIs(l.find(2), None)
        n = [Node(0), Node(1), Node(2), Node(3), Node(2)]
        addToList(l, n)
        self.assertIs(l.find(2), n[2])
        self.assertIs(l.find(42), None)

    def test_find_all(self):
        l = LinkedList()
        self.assertListEqual(l.find_all(2), [])
        n = [Node(0), Node(1), Node(2), Node(3), Node(2)]
        addToList(l, n)
        self.assertListEqual(l.find_all(2), [n[2], n[4]])
        self.assertListEqual(l.find_all(42), [])
        self.assertListEqual(l.find_all(3), [n[3]])

    def test_delete(self):
        l = LinkedList()
        n = [Node(0), Node(1), Node(2), Node(3), Node(2)]
        addToList(l, n)
        l.delete(42)
        checkList(self, l, n)
        l.delete(2)
        checkList(self, l, n[:2] + n[3:])
        l.delete(2)
        checkList(self, l, n[:2] + n[3:4])
        l.delete(0)
        checkList(self, l, [n[1], n[3]])
        l.delete(1)
        checkList(self, l, [n[3]])
        l.delete(1)
        checkList(self, l, [n[3]])
        l.delete(3)
        checkList(self, l, [])
        l.delete(3)
        checkList(self, l, [])

    def test_delete_all(self):
        l = LinkedList()
        n = [Node(0), Node(0), Node(1), Node(1), Node(4), Node(2), Node(3), Node(3), Node(2)]
        addToList(l, n)
        l.delete(42, all=True)
        checkList(self, l, n)
        l.delete(2, all=True)
        checkList(self, l, n[:5] + n[6:8])
        l.delete(1, all=True)
        checkList(self, l, n[:2] + n[4:5] + n[6:8])
        l.delete(0, all=True)
        checkList(self, l, n[4:5] + n[6:8])
        l.delete(3, all=True)
        checkList(self, l, n[4:5])
        l.delete(3, all=True)
        checkList(self, l, n[4:5])
        l.delete(4, all=True)
        checkList(self, l, [])
        l.delete(4, all=True)
        checkList(self, l, [])
        for node in n[:2]:
            l.add_in_tail(node)
        l.delete(0, all=True)
        checkList(self, l, [])

    def test_clean(self):
        l = LinkedList()
        l.clean()
        checkList(self, l, [])
        addToList(l, [Node(1), Node(2)])
        l.clean()
        checkList(self, l, [])
    
    def test_len(self):
        l = LinkedList()
        self.assertEqual(l.len(), 0)
        l.add_in_tail(Node(1))
        self.assertEqual(l.len(), 1)
        l.add_in_tail(Node(2))
        self.assertEqual(l.len(), 2)

    def test_insert(self):
        l = LinkedList()
        n = [Node(0), Node(1), Node(2), Node(3)]
        l.insert(None, n[1])
        checkList(self, l, n[1:2])
        l.insert(None, n[0])
        checkList(self, l, n[:2])
        l.insert(n[1], n[3])
        checkList(self, l, n[:2] + n[3:])
        l.insert(n[1], n[2])
        checkList(self, l, n)


from linked_list_x import addLinkedList

class TestX(unittest.TestCase):
    
    def test(self):
        a = LinkedList()
        b = LinkedList()
        checkList(self, addLinkedList(a, b), [])
        addToList(a, [Node(1), Node(2), Node(3)])
        self.assertIsNone(addLinkedList(a, b))
        self.assertIsNone(addLinkedList(b, a))
        addToList(b, [Node(10), Node(20)])
        self.assertIsNone(addLinkedList(a, b))
        self.assertIsNone(addLinkedList(b, a))
        b.add_in_tail(Node(30))
        c = addLinkedList(a, b)
        d = addLinkedList(b, a)
        na = a.head
        nb = b.head
        nc = c.head
        nd = d.head
        while na is not None:
            self.assertEqual(nc.value, na.value + nb.value)
            self.assertEqual(nd.value, nc.value)
            na = na.next
            nb = nb.next
            nc = nc.next
            nd = nd.next
        self.assertIsNone(na)
        self.assertIsNone(nb)
        self.assertIsNone(nc)
        self.assertIsNone(nd)


if __name__ == '__main__':
    unittest.main()
