import unittest

from bloom_filter import BloomFilter


class Test(unittest.TestCase):

    def test_empty(self):
        bf = BloomFilter(32)
        self.assertFalse(bf.is_value("0123456789"))
        self.assertFalse(bf.is_value("1234567890"))
        self.assertFalse(bf.is_value("2345678901"))
        self.assertFalse(bf.is_value("3456789012"))
        self.assertFalse(bf.is_value("4567890123"))
        self.assertFalse(bf.is_value("5678901234"))
        self.assertFalse(bf.is_value("6789012345"))
        self.assertFalse(bf.is_value("7890123456"))
        self.assertFalse(bf.is_value("8901234567"))
        self.assertFalse(bf.is_value("9012345678"))

    def test_some(self):
        bf = BloomFilter(32)
        bf.add("0123456789")
        bf.add("2345678901")
        bf.add("5678901234")
        bf.add("6789012345")
        bf.add("9012345678")
        self.assertTrue(bf.is_value("0123456789"))
        self.assertTrue(bf.is_value("2345678901"))
        self.assertTrue(bf.is_value("5678901234"))
        self.assertTrue(bf.is_value("6789012345"))
        self.assertTrue(bf.is_value("9012345678"))

    def test_full(self):
        bf = BloomFilter(32)
        bf.add("0123456789")
        bf.add("1234567890")
        bf.add("2345678901")
        bf.add("3456789012")
        bf.add("4567890123")
        bf.add("5678901234")
        bf.add("6789012345")
        bf.add("7890123456")
        bf.add("8901234567")
        bf.add("9012345678")
        self.assertTrue(bf.is_value("0123456789"))
        self.assertTrue(bf.is_value("1234567890"))
        self.assertTrue(bf.is_value("2345678901"))
        self.assertTrue(bf.is_value("3456789012"))
        self.assertTrue(bf.is_value("4567890123"))
        self.assertTrue(bf.is_value("5678901234"))
        self.assertTrue(bf.is_value("6789012345"))
        self.assertTrue(bf.is_value("7890123456"))
        self.assertTrue(bf.is_value("8901234567"))
        self.assertTrue(bf.is_value("9012345678"))


if __name__ == "__main__":
    unittest.main()
