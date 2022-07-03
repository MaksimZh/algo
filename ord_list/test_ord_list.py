import unittest

from ord_list import OrderedList

class TestOrderedList(unittest.TestCase):

    def checkList(self, l, test):
        nodes = l.get_all()
        for i in range(1, len(nodes)):
            self.assertIs(nodes[i].prev, nodes[i - 1])
            self.assertIs(nodes[i - 1].next, nodes[i])
        vals = [node.value for node in nodes]
        self.assertListEqual(vals, test)

    def test_compare(self):
        ol = OrderedList(asc=True)
        self.assertEqual(ol.compare(5, 6), -1)
        self.assertEqual(ol.compare(5, 5), 0)
        self.assertEqual(ol.compare(5, 4), 1)

    def test_asc_0(self):
        ol = OrderedList(asc=True)
        self.checkList(ol, [])

    def test_asc_1(self):
        ol = OrderedList(asc=True)
        ol.add(5)
        self.checkList(ol, [5])

    def test_desc_1(self):
        ol = OrderedList(asc=False)
        ol.add(5)
        self.checkList(ol, [5])


if __name__ == "__main__":
    unittest.main()
