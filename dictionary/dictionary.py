class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(ord(c) for c in key) % self.size

    def __seek_slot(self, key):
        s = self.hash_fun(key)
        for i in range(self.size):
            if (self.slots[s] is None) or (self.slots[s] == key):
                return s
            s += 1
            if s >= self.size:
                s %= self.size
        return None

    def is_key(self, key):
        s = self.__seek_slot(key)
        return (s is not None) and (self.slots[s] is not None)

    def put(self, key, value):
        s = self.__seek_slot(key)
        self.slots[s] = key
        self.values[s] = value

    def get(self, key):
        s = self.__seek_slot(key)
        if s is None:
            return None
        else:
            return self.values[s]
