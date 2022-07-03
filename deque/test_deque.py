import unittest

from deque import Deque
from palindrom import isPalindrom

class TestQueue(unittest.TestCase):

    def test_0(self):
        d = Deque()
        self.assertEqual(d.size(), 0)
        self.assertIsNone(d.removeFront())
        self.assertEqual(d.size(), 0)
        self.assertIsNone(d.removeTail())
        self.assertEqual(d.size(), 0)

    def test_1(self):
        d = Deque()
        d.addFront(5)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.removeFront(), 5)
        self.assertEqual(d.size(), 0)
        d.addFront(6)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.removeTail(), 6)
        self.assertEqual(d.size(), 0)
        d.addTail(7)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.removeFront(), 7)
        self.assertEqual(d.size(), 0)
        d.addTail(8)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.removeTail(), 8)
        self.assertEqual(d.size(), 0)

    def test_10(self):
        d = Deque()
        self.assertEqual(d.size(), 0)
        d.addFront(1)
        self.assertEqual(d.size(), 1)
        d.addFront(2)
        self.assertEqual(d.size(), 2)
        d.addFront(3)
        self.assertEqual(d.size(), 3)
        d.addFront(4)
        self.assertEqual(d.size(), 4)
        self.assertEqual(d.removeFront(), 4)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.removeFront(), 3)
        self.assertEqual(d.size(), 2)
        d.addFront(5)
        self.assertEqual(d.size(), 3)
        d.addFront(6)
        self.assertEqual(d.size(), 4)
        d.addFront(7)
        self.assertEqual(d.size(), 5)
        d.addFront(8)
        self.assertEqual(d.size(), 6)
        self.assertEqual(d.removeTail(), 1)
        self.assertEqual(d.size(), 5)
        self.assertEqual(d.removeTail(), 2)
        self.assertEqual(d.size(), 4)
        d.addTail(9)
        self.assertEqual(d.size(), 5)
        d.addTail(10)
        self.assertEqual(d.size(), 6)
        self.assertEqual(d.removeFront(), 8)
        self.assertEqual(d.size(), 5)
        self.assertEqual(d.removeFront(), 7)
        self.assertEqual(d.size(), 4)
        self.assertEqual(d.removeFront(), 6)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.removeFront(), 5)
        self.assertEqual(d.size(), 2)
        d.addTail(11)
        self.assertEqual(d.size(), 3)
        d.addTail(12)
        self.assertEqual(d.size(), 4)
        self.assertEqual(d.removeTail(), 12)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.removeTail(), 11)
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.removeTail(), 10)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.removeTail(), 9)
        self.assertEqual(d.size(), 0)


class TestPalindrom(unittest.TestCase):

    def test(self):
        self.assertTrue(isPalindrom(""))
        self.assertTrue(isPalindrom("a"))
        self.assertTrue(isPalindrom("aba"))
        self.assertTrue(isPalindrom("abcacbcacba"))
        self.assertFalse(isPalindrom("ab"))
        self.assertFalse(isPalindrom("abab"))
        self.assertFalse(isPalindrom("aaba"))
        self.assertFalse(isPalindrom("abacbcacba"))


if __name__ == "__main__":
    unittest.main()
