import unittest

from ord_list import OrderedList

class TestOrderedList(unittest.TestCase):

    def test_compare(self):
        ol = OrderedList(asc=True)
        self.assertEqual(ol.compare(5, 6), -1)
        self.assertEqual(ol.compare(5, 5), 0)
        self.assertEqual(ol.compare(5, 4), 1)



if __name__ == "__main__":
    unittest.main()
