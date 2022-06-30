import unittest

from queue import Queue

class Test(unittest.TestCase):

    def test_0(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        self.assertIsNone(q.dequeue())
        self.assertEqual(q.size(), 0)

    def test_1(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertIsNone(q.dequeue())
        self.assertEqual(q.size(), 0)

    def test_10(self):
        q = Queue()
        for i in range(1, 11):
            q.enqueue(i)
        for i in range(1, 11):
            self.assertEqual(q.size(), 11 - i)
            self.assertEqual(q.dequeue(), i)


if __name__ == '__main__':
    unittest.main()
