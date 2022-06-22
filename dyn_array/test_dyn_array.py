import unittest

from dyn_array import DynArray


def addItems(a, items):
    for i in items:
        a.append(i)

class Test(unittest.TestCase):

    def checkArray(self, a, cap, test):
        self.assertEqual(a.capacity, cap)
        self.assertEqual(len(a), len(test))
        for i in range(len(a)):
            self.assertEqual(a[i], test[i])

    def test_fill(self):
        a = DynArray()
        self.checkArray(a, 16, [])
        a.append(0)
        self.checkArray(a, 16, [0])
        a.append(1)
        self.checkArray(a, 16, [0, 1])
        addItems(a, range(2, 5))
        self.checkArray(a, 16, range(0, 5))
        addItems(a, range(5, 16))
        self.checkArray(a, 16, range(0, 16))
        a.append(16)
        self.checkArray(a, 32, range(0, 17))

    def test_insert(self):
        a = DynArray()
        self.assertRaises(IndexError, a.insert, -1, 42)
        self.assertRaises(IndexError, a.insert, 1, 42)
        a.insert(0, 1)
        self.checkArray(a, 16, [1])
        self.assertRaises(IndexError, a.insert, -2, 42)
        self.assertRaises(IndexError, a.insert, 2, 42)
        a.insert(0, 2)
        self.checkArray(a, 16, [2, 1])
        a.insert(1, 3)
        self.checkArray(a, 16, [2, 3, 1])
        self.assertRaises(IndexError, a.insert, -100, 42)
        self.assertRaises(IndexError, a.insert, 100, 42)
        a.insert(3, 4)
        self.checkArray(a, 16, [2, 3, 1, 4])
        a = DynArray()
        addItems(a, range(0, 16))
        a.insert(0, 42)
        self.checkArray(a, 32, [42, *range(0, 16)])
        a = DynArray()
        addItems(a, range(0, 16))
        a.insert(10, 42)
        self.checkArray(a, 32, [*range(0, 10), 42, *range(10, 16)])
        a = DynArray()
        addItems(a, range(0, 16))
        a.insert(16, 42)
        self.checkArray(a, 32, [*range(0, 16), 42])

    def test_delete(self):
        a = DynArray()
        self.assertRaises(IndexError, a.delete, -1)
        self.assertRaises(IndexError, a.delete, 0)
        a.insert(0, 1)
        self.assertRaises(IndexError, a.delete, -1)
        self.assertRaises(IndexError, a.delete, 1)
        a.delete(0)
        self.checkArray(a, 16, [])
        addItems(a, range(0, 5))
        self.assertRaises(IndexError, a.delete, -10)
        self.assertRaises(IndexError, a.delete, 10)
        a.delete(0)
        self.checkArray(a, 16, range(1, 5))
        a.delete(3)
        self.checkArray(a, 16, range(1, 4))
        a.delete(1)
        self.checkArray(a, 16, [1, 3])
        a = DynArray()
        addItems(a, range(0, 20))
        self.assertRaises(IndexError, a.delete, -100)
        self.assertRaises(IndexError, a.delete, 100)
        a.delete(0)
        self.checkArray(a, 32, range(1, 20))
        a.delete(18)
        self.checkArray(a, 32, range(1, 19))
        a.delete(3)
        self.checkArray(a, 32, [1, 2, 3, *range(5, 19)])
        a.delete(2)
        self.checkArray(a, 32, [1, 2, *range(5, 19)])
        a.delete(1)
        self.checkArray(a, 21, [1, *range(5, 19)])


if __name__ == '__main__':
    unittest.main()
