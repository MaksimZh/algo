class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        return self.__hash(str1, 17)

    def hash2(self, str1):
        return self.__hash(str1, 223)

    def __hash(self, str1, factor):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * factor + code) % self.filter_len
        return 1 << result

    def add(self, str1):
        self.filter |= self.hash1(str1)
        self.filter |= self.hash2(str1)

    def is_value(self, str1):
        f1 = self.filter & self.hash1(str1)
        f2 = self.filter & self.hash2(str1)
        return f1 > 0 and f2 > 0
