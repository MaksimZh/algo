import unittest


class AbstractTest(unittest.TestCase):

    def test_0(self):
        s = self.Stack()
        self.assertEqual(s.size(), 0)
        self.assertIsNone(s.peek())
        self.assertEqual(s.size(), 0)
        self.assertIsNone(s.pop())
        self.assertEqual(s.size(), 0)
    
    def test_1(self):
        s = self.Stack()
        s.push(1)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.size(), 0)
        self.assertIsNone(s.peek())
        self.assertIsNone(s.pop())

    def test_10(self):
        s = self.Stack()
        for i in range(1, 11):
            s.push(i)
        for i in range(10, 0, -1):
            self.assertEqual(s.size(), i)
            self.assertEqual(s.peek(), i)
            self.assertEqual(s.size(), i)
            self.assertEqual(s.pop(), i)

import stack
class Test(AbstractTest):
    Stack = stack.Stack

import stack_a
class TestA(AbstractTest):
    Stack = stack_a.Stack

del AbstractTest

if __name__ == '__main__':
    unittest.main()
