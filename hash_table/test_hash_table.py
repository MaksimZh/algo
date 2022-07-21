import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ch = "abcdefghijklmnopqrstuvwxyz"
        cls.values = [ch[i : i + 2] for i in range(len(ch) - 1)]

    def test_hash_fun(self):
        ht = HashTable(sz=17, stp=3)
        hashes = [ht.hash_fun(v) for v in self.values]
        found = [False] * ht.size
        for h in hashes:
            found[h] = True
            self.assertTrue(h >= 0 and h < ht.size)
        self.assertTrue(all(found))

    def test_seek_slot_put(self):
        ht = HashTable(sz=7, stp=3)
        ss = []
        for v in self.values:
            s = ht.seek_slot(v)
            p = ht.put(v)
            self.assertEqual(s, p)
            ss.append(s)
        self.assertListEqual(sorted(ss[:ht.size]), list(range(0, ht.size)))
        for s in ss[ht.size:]:
            self.assertIsNone(s)

    def test_find(self):
        ht = HashTable(sz=17, stp=3)
        self.assertIsNone(ht.find("5"))
        ht.put("5")
        self.assertIsNone(ht.find("42"))
        i = ht.find("5")
        self.assertTrue(i >= 0 and i < ht.size)
        ht.put("7")
        self.assertIsNone(ht.find("42"))
        i = ht.find("5")
        self.assertTrue(i >= 0 and i < ht.size)
        i = ht.find("7")
        self.assertTrue(i >= 0 and i < ht.size)


if __name__ == "__main__":
    unittest.main()
