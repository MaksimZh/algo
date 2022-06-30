import unittest


class AbstractTest(unittest.TestCase):

    def test_0(self):
        q = self.Queue()
        self.assertEqual(q.size(), 0)
        self.assertIsNone(q.dequeue())
        self.assertEqual(q.size(), 0)

    def test_1(self):
        q = self.Queue()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertIsNone(q.dequeue())
        self.assertEqual(q.size(), 0)

    def test_10(self):
        q = self.Queue()
        for i in range(1, 11):
            q.enqueue(i)
        for i in range(1, 11):
            self.assertEqual(q.size(), 11 - i)
            self.assertEqual(q.dequeue(), i)

    def test_10_x(self):
        q = self.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.size(), 2)
        q.enqueue(6)
        q.enqueue(7)
        q.enqueue(8)
        q.enqueue(9)
        q.enqueue(10)
        self.assertEqual(q.size(), 7)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 6)
        self.assertEqual(q.dequeue(), 7)
        self.assertEqual(q.dequeue(), 8)
        self.assertEqual(q.dequeue(), 9)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.size(), 0)

import queue
class Test(AbstractTest):
    Queue = queue.Queue

import queue_stack
class TestStack(AbstractTest):
    Queue = queue_stack.Queue

del AbstractTest

if __name__ == '__main__':
    unittest.main()
