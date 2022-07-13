import unittest

from cache import NativeCache


class Test(unittest.TestCase):

    def test_fill(self):
        d = NativeCache(6)
        kv = {
            "abc": 1,
            "def": 2,
            "aec": 3,
            "bca": 4,
            "edf": 5,
            "fcd": 6,
        }
        self.assertFalse(d.is_key("abc"))
        self.assertIsNone(d.get("abc"))
        for k, v in kv.items():
            d.put(k, v)
        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)
        kv["bca"] = 42
        d.put("bca", 42)
        kv["def"] = 43
        d.put("def", 43)
        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)
        self.assertFalse(d.is_key("foo"))
        self.assertIsNone(d.get("foo"))

    def test_drop(self):
        d = NativeCache(6)
        kv = {
            "abc": 1,
            "def": 2,
            "aec": 3,
            "bca": 4,
            "edf": 5,
            "fcd": 6,
        }
        for k, v in kv.items():
            d.put(k, v)
        for k, v in kv.items():
            for i in range(v):
                d.get(k)
        d.put("fab", 42)
        del kv["abc"]
        kv["fab"] = 42
        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)
        self.assertFalse(d.is_key("abc"))
        for i in range(7):
            d.get("fab")
        d.put("feb", 43)
        d.put("fed", 44)
        del kv["def"]
        kv["fed"] = 44
        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)
        self.assertFalse(d.is_key("def"))
        self.assertFalse(d.is_key("feb"))

if __name__ == "__main__":
    unittest.main()
