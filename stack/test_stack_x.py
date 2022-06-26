import unittest

from stack import Stack
from stack_x import paren_balanced, stack_eval


class Test(unittest.TestCase):

    def test_paren_balanced(self):
        self.assertTrue(paren_balanced(""))
        self.assertTrue(paren_balanced("()"))
        self.assertTrue(paren_balanced("(())"))
        self.assertTrue(paren_balanced("(()())"))
        self.assertTrue(paren_balanced("(()(()))"))
        self.assertFalse(paren_balanced("("))
        self.assertFalse(paren_balanced(")"))
        self.assertFalse(paren_balanced(")("))
        self.assertFalse(paren_balanced("(()((()))()))"))

    def test_stack_eval_1(self):
        s = Stack()
        s.push("*")
        s.push(3)
        s.push("+")
        s.push(2)
        s.push(1)
        self.assertEqual(stack_eval(s), 9)

    def test_stack_eval_2(self):
        s = Stack()
        s.push("=")
        s.push("+")
        s.push(9)
        s.push("*")
        s.push(5)
        s.push("+")
        s.push(2)
        s.push(8)
        self.assertEqual(stack_eval(s), 59)


if __name__ == '__main__':
    unittest.main()
