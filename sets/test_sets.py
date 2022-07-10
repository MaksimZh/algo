import unittest

from sets import PowerSet


class Test(unittest.TestCase):

    def test_empty(self):
        s = PowerSet()
        self.assertEqual(s.size(), 0)
        self.assertFalse(s.get(42))
        self.assertFalse(s.remove(42))

    def test_one(self):
        s = PowerSet()
        s.put(1)
        self.assertEqual(s.size(), 1)
        self.assertTrue(s.get(1))
        self.assertFalse(s.get(42))
        self.assertFalse(s.remove(42))
        s.put(1)
        self.assertEqual(s.size(), 1)
        self.assertTrue(s.get(1))
        self.assertFalse(s.get(42))
        self.assertTrue(s.remove(1))
        self.assertEqual(s.size(), 0)

    def test_many(self):
        s = PowerSet()
        for i in range(20000):
            s.put(i)
        self.assertEqual(s.size(), 20000)
        for i in range(20000):
            self.assertTrue(s.get(i))
        for i in range(20000):
            self.assertTrue(s.remove(i))
        self.assertEqual(s.size(), 0)

    def test_intersection(self):
        a = PowerSet()
        for i in [1, 2, 3, 4, 5]:
            a.put(i)
        b = PowerSet()
        for i in [3, 5, 7, 9]:
            b.put(i)
        c = PowerSet()
        d = PowerSet()
        for i in [6, 7, 8, 9]:
            d.put(i)

        r = a.intersection(b)
        self.assertEqual(r.size(), 2)
        for i in [3, 5]:
            self.assertTrue(r.get(i))
        
        r = b.intersection(a)
        self.assertEqual(r.size(), 2)
        for i in [3, 5]:
            self.assertTrue(r.get(i))

        r = a.intersection(c)
        self.assertEqual(r.size(), 0)

        r = c.intersection(a)
        self.assertEqual(r.size(), 0)

        r = a.intersection(d)
        self.assertEqual(r.size(), 0)

        r = c.intersection(d)
        self.assertEqual(r.size(), 0)


if __name__ == "__main__":
    unittest.main()
