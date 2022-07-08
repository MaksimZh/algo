import unittest

from dictionary import NativeDictionary


class Test(unittest.TestCase):

    def test(self):
        d = NativeDictionary(6)
        kv = {
            "aa": 1,
            "bb": 2,
            "cc": 3,
            "dd": 4,
            "ee": 5,
            "ff": 6,
        }
        self.assertFalse(d.is_key("aa"))
        self.assertIsNone(d.get("aa"))
        for k, v in kv.items():
            d.put(k, v)
        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)
        kv["bb"] = 42
        d.put("bb", 42)
        kv["ee"] = 43
        d.put("ee", 43)
        for k, v in kv.items():
            self.assertTrue(d.is_key(k))
            self.assertEqual(d.get(k), v)
        self.assertFalse(d.is_key("foo"))
        self.assertIsNone(d.get("foo"))

if __name__ == "__main__":
    unittest.main()
