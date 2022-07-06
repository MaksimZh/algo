class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(ord(c) for c in value) % self.size

    def seek_slot(self, value):
        s = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[s] is None:
                return s
            s += self.step
            if s >= self.size:
                s %= self.size
        return None

    def put(self, value):
        s = self.seek_slot(value)
        if s is not None:
            self.slots[s] = value
        return s

    def find(self, value):
        s = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[s] == value:
                return s
            s += self.step
            if s >= self.size:
                s %= self.size
        return None
