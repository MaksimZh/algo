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


if __name__ == "__main__":
    unittest.main()
