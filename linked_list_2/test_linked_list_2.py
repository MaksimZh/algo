import unittest

from linked_list_2 import Node, LinkedList2


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
        n = [Node(0), Node(1)]
        self.checkList(l, [])
        l.add_in_tail(n[0])
        self.checkList(l, n[0:1])
        l.add_in_tail(n[1])
        self.checkList(l, n)


if __name__ == '__main__':
    unittest.main()
