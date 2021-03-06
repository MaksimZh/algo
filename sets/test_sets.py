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
            self.assertEqual(s.size(), i + 1)
        for i in range(20000):
            self.assertTrue(s.get(i))
        for i in range(20000):
            self.assertTrue(s.remove(i))
            self.assertEqual(s.size(), 20000 - i - 1)


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
        e = PowerSet()
        for i in [2, 3, 4]:
            e.put(i)

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

        r = d.intersection(a)
        self.assertEqual(r.size(), 0)

        r = a.intersection(e)
        self.assertEqual(r.size(), 3)
        for i in [2, 3, 4]:
            self.assertTrue(r.get(i))

        r = e.intersection(a)
        self.assertEqual(r.size(), 3)
        for i in [2, 3, 4]:
            self.assertTrue(r.get(i))


    def test_union(self):
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
        e = PowerSet()
        for i in [2, 3, 4]:
            e.put(i)
        
        r = a.union(b)
        self.assertEqual(r.size(), 7)
        for i in [1, 2, 3, 4, 5, 7, 9]:
            self.assertTrue(r.get(i))
        
        r = b.union(a)
        self.assertEqual(r.size(), 7)
        for i in [1, 2, 3, 4, 5, 7, 9]:
            self.assertTrue(r.get(i))

        r = a.union(c)
        self.assertEqual(r.size(), 5)
        for i in [1, 2, 3, 4, 5]:
            self.assertTrue(r.get(i))

        r = c.union(a)
        self.assertEqual(r.size(), 5)
        for i in [1, 2, 3, 4, 5]:
            self.assertTrue(r.get(i))

        r = a.union(d)
        self.assertEqual(r.size(), 9)
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.assertTrue(r.get(i))

        r = d.union(a)
        self.assertEqual(r.size(), 9)
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.assertTrue(r.get(i))

        r = a.union(e)
        self.assertEqual(r.size(), 5)
        for i in [1, 2, 3, 4, 5]:
            self.assertTrue(r.get(i))

        r = e.union(a)
        self.assertEqual(r.size(), 5)
        for i in [1, 2, 3, 4, 5]:
            self.assertTrue(r.get(i))


    def test_difference(self):
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
        e = PowerSet()
        for i in [2, 3, 4]:
            e.put(i)
        
        r = a.difference(b)
        self.assertEqual(r.size(), 3)
        for i in [1, 2, 4]:
            self.assertTrue(r.get(i))
        
        r = b.difference(a)
        self.assertEqual(r.size(), 2)
        for i in [7, 9]:
            self.assertTrue(r.get(i))

        r = a.difference(c)
        self.assertEqual(r.size(), 5)
        for i in [1, 2, 3, 4, 5]:
            self.assertTrue(r.get(i))

        r = c.difference(a)
        self.assertEqual(r.size(), 0)

        r = a.difference(d)
        self.assertEqual(r.size(), 5)
        for i in [1, 2, 3, 4, 5]:
            self.assertTrue(r.get(i))

        r = d.difference(a)
        self.assertEqual(r.size(), 4)
        for i in [6, 7, 8, 9]:
            self.assertTrue(r.get(i))

        r = a.difference(e)
        self.assertEqual(r.size(), 2)
        for i in [1, 5]:
            self.assertTrue(r.get(i))

        r = e.difference(a)
        self.assertEqual(r.size(), 0)


    def test_issubset(self):
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
        e = PowerSet()
        for i in [2, 3, 4]:
            e.put(i)
        
        self.assertFalse(a.issubset(b))
        self.assertFalse(b.issubset(a))
        self.assertTrue(a.issubset(c))
        self.assertFalse(c.issubset(a))
        self.assertFalse(a.issubset(d))
        self.assertFalse(d.issubset(a))
        self.assertTrue(a.issubset(e))
        self.assertFalse(e.issubset(a))


if __name__ == "__main__":
    unittest.main()
