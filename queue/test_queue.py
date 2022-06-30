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

import queue
class Test(AbstractTest):
    Queue = queue.Queue

import queue_stack
class TestStack(AbstractTest):
    Queue = queue_stack.Queue

del AbstractTest

if __name__ == '__main__':
    unittest.main()
