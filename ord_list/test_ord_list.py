import unittest

from ord_list import OrderedList, OrderedStringList


class TestOrderedList(unittest.TestCase):

    def ListType(self):
        return OrderedList

    def checkList(self, ol, test):
        self.assertEqual(ol.len(), len(test))
        nodes = ol.get_all()
        if len(nodes) > 0:
            self.assertIs(ol.head, nodes[0])
            self.assertIs(ol.tail, nodes[-1])
            self.assertIsNone(nodes[0].prev)
            self.assertIsNone(nodes[-1].next)
        else:
            self.assertIsNone(ol.head)
            self.assertIsNone(ol.tail)
        for i in range(1, len(nodes)):
            self.assertIs(nodes[i].prev, nodes[i - 1])
            self.assertIs(nodes[i - 1].next, nodes[i])
        vals = [node.value for node in nodes]
        self.assertListEqual(vals, test)

    def checkAscending(self, ol):
        self.checkList(ol, [])
        self.assertIsNone(ol.find(42))
        ol.delete(42)
        self.checkList(ol, [])
        ol.add(5)
        self.checkList(ol, [5])
        self.assertIsNone(ol.find(42))
        self.assertIsNotNone(ol.find(5))
        ol.delete(5)
        self.checkList(ol, [])
        ol.add(5)
        ol.add(3)
        self.checkList(ol, [3, 5])
        ol.add(7)
        self.checkList(ol, [3, 5, 7])
        ol.add(4)
        self.checkList(ol, [3, 4, 5, 7])
        ol.add(6)
        self.checkList(ol, [3, 4, 5, 6, 7])
        self.assertIsNone(ol.find(42))
        self.assertIsNotNone(ol.find(3))
        self.assertIsNotNone(ol.find(4))
        self.assertIsNotNone(ol.find(5))
        self.assertIsNotNone(ol.find(6))
        self.assertIsNotNone(ol.find(7))
        ol.delete(5)
        self.checkList(ol, [3, 4, 6, 7])
        ol.delete(3)
        self.checkList(ol, [4, 6, 7])
        ol.delete(7)
        self.checkList(ol, [4, 6])

    def checkDescending(self, ol):
        self.checkList(ol, [])
        self.assertIsNone(ol.find(42))
        ol.delete(42)
        self.checkList(ol, [])
        ol.add(5)
        self.checkList(ol, [5])
        self.assertIsNone(ol.find(42))
        self.assertIsNotNone(ol.find(5))
        ol.delete(5)
        self.checkList(ol, [])
        ol.add(5)
        ol.add(3)
        self.checkList(ol, [5, 3])
        ol.add(7)
        self.checkList(ol, [7, 5, 3])
        ol.add(4)
        self.checkList(ol, [7, 5, 4, 3])
        ol.add(6)
        self.checkList(ol, [7, 6, 5, 4, 3])
        self.assertIsNone(ol.find(42))
        self.assertIsNotNone(ol.find(3))
        self.assertIsNotNone(ol.find(4))
        self.assertIsNotNone(ol.find(5))
        self.assertIsNotNone(ol.find(6))
        self.assertIsNotNone(ol.find(7))
        ol.delete(5)
        self.checkList(ol, [7, 6, 4, 3])
        ol.delete(3)
        self.checkList(ol, [7, 6, 4])
        ol.delete(7)
        self.checkList(ol, [6, 4])
    
    def test_compare(self):
        ol = self.ListType()(asc=True)
        self.assertEqual(ol.compare(5, 6), -1)
        self.assertEqual(ol.compare(5, 5), 0)
        self.assertEqual(ol.compare(5, 4), 1)

    def test_asc(self):
        ol = self.ListType()(asc=True)
        self.checkAscending(ol)
        ol.clean(asc=True)
        self.checkAscending(ol)
        ol.clean(asc=False)
        self.checkDescending(ol)

    def test_desc(self):
        ol = OrderedList(asc=False)
        self.checkDescending(ol)
        ol.clean(asc=False)
        self.checkDescending(ol)
        ol.clean(asc=True)
        self.checkAscending(ol)


class TestOrderedStringList(TestOrderedList):
    
    def ListType(self):
        return OrderedStringList

    def checkAscending(self, ol):
        self.checkList(ol, [])
        self.assertIsNone(ol.find("42"))
        ol.delete("42")
        self.checkList(ol, [])
        ol.add("5")
        self.checkList(ol, ["5"])
        self.assertIsNone(ol.find("42"))
        self.assertIsNotNone(ol.find("5"))
        ol.delete("5")
        self.checkList(ol, [])
        ol.add("5")
        ol.add("3")
        self.checkList(ol, ["3", "5"])
        ol.add("7")
        self.checkList(ol, ["3", "5", "7"])
        ol.add("4")
        self.checkList(ol, ["3", "4", "5", "7"])
        ol.add("6")
        self.checkList(ol, ["3", "4", "5", "6", "7"])
        self.assertIsNone(ol.find("42"))
        self.assertIsNotNone(ol.find("3"))
        self.assertIsNotNone(ol.find("4"))
        self.assertIsNotNone(ol.find("5"))
        self.assertIsNotNone(ol.find("6"))
        self.assertIsNotNone(ol.find("7"))
        ol.delete("5")
        self.checkList(ol, ["3", "4", "6", "7"])
        ol.delete("3")
        self.checkList(ol, ["4", "6", "7"])
        ol.delete("7")
        self.checkList(ol, ["4", "6"])

    def checkDescending(self, ol):
        self.checkList(ol, [])
        self.assertIsNone(ol.find("42"))
        ol.delete("42")
        self.checkList(ol, [])
        ol.add("5")
        self.checkList(ol, ["5"])
        self.assertIsNone(ol.find("42"))
        self.assertIsNotNone(ol.find("5"))
        ol.delete("5")
        self.checkList(ol, [])
        ol.add("5")
        ol.add("3")
        self.checkList(ol, ["5", "3"])
        ol.add("7")
        self.checkList(ol, ["7", "5", "3"])
        ol.add("4")
        self.checkList(ol, ["7", "5", "4", "3"])
        ol.add("6")
        self.checkList(ol, ["7", "6", "5", "4", "3"])
        self.assertIsNone(ol.find("42"))
        self.assertIsNotNone(ol.find("3"))
        self.assertIsNotNone(ol.find("4"))
        self.assertIsNotNone(ol.find("5"))
        self.assertIsNotNone(ol.find("6"))
        self.assertIsNotNone(ol.find("7"))
        ol.delete("5")
        self.checkList(ol, ["7", "6", "4", "3"])
        ol.delete("3")
        self.checkList(ol, ["7", "6", "4"])
        ol.delete("7")
        self.checkList(ol, ["6", "4"])

    def test_compare(self):
        ol = self.ListType()(asc=True)
        self.assertEqual(ol.compare("", ""), 0)
        self.assertEqual(ol.compare(" ", " "), 0)
        self.assertEqual(ol.compare("", " "), 0)
        
        self.assertEqual(ol.compare("", "a"), -1)
        self.assertEqual(ol.compare("a", "a"), 0)
        self.assertEqual(ol.compare("a", ""), 1)

        self.assertEqual(ol.compare("  ", "a"), -1)
        self.assertEqual(ol.compare("  a ", " a   "), 0)
        self.assertEqual(ol.compare(" a ", "   "), 1)

        self.assertEqual(ol.compare("a", "ab"), -1)
        self.assertEqual(ol.compare("ab", "ab"), 0)
        self.assertEqual(ol.compare("ab", "a"), 1)

        self.assertEqual(ol.compare("  a", "ab"), -1)
        self.assertEqual(ol.compare("ab   ", "ab "), 0)
        self.assertEqual(ol.compare(" ab   ", " a  "), 1)


from ord_list import trim

class TestTrim(unittest.TestCase):

    def test(self):
        self.assertEqual(trim(""), "")
        self.assertEqual(trim(" "), "")
        self.assertEqual(trim("   "), "")
        self.assertEqual(trim("abc"), "abc")
        self.assertEqual(trim("   abc"), "abc")
        self.assertEqual(trim("abc  "), "abc")
        self.assertEqual(trim("   abc  "), "abc")


if __name__ == "__main__":
    unittest.main()
