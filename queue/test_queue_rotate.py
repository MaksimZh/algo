import unittest

from queue import Queue
from queue_rotate import rotateQueue

def readQueue(q):
    return [q.dequeue() for i in range(q.size())]

class Test(unittest.TestCase):

    def test_0(self):
        q = Queue()
        rotateQueue(q, 0)
        self.assertEqual(q.size(), 0)
        rotateQueue(q, 1)
        self.assertEqual(q.size(), 0)
        rotateQueue(q, 2)
        self.assertEqual(q.size(), 0)

    def test_1(self):
        q = Queue()
        q.enqueue(1)
        rotateQueue(q, 0)
        self.assertEqual(readQueue(q), [1])
        q.enqueue(1)
        rotateQueue(q, 1)
        self.assertEqual(readQueue(q), [1])
        q.enqueue(1)
        rotateQueue(q, 2)
        self.assertEqual(readQueue(q), [1])

    def test_5(self):
        q = Queue()
        for i in range(1, 6):
            q.enqueue(i)
        rotateQueue(q, 0)
        self.assertEqual(readQueue(q), [1, 2, 3, 4, 5])
        for i in range(1, 6):
            q.enqueue(i)
        rotateQueue(q, 1)
        self.assertEqual(readQueue(q), [2, 3, 4, 5, 1])
        for i in range(1, 6):
            q.enqueue(i)
        rotateQueue(q, 2)
        self.assertEqual(readQueue(q), [3, 4, 5, 1, 2])
        for i in range(1, 6):
            q.enqueue(i)
        rotateQueue(q, 8)
        self.assertEqual(readQueue(q), [4, 5, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
