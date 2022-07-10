class PowerSet:

    def __init__(self):
        self.items = {}

    def size(self):
        return len(self.items)

    def put(self, value):
        self.items[value] = True

    def get(self, value):
        return value in self.items

    def remove(self, value):
        if value in self.items:
            del self.items[value]
            return True
        else:
            return False

    def intersection(self, set2):
        result = PowerSet()
        for key in self.items.keys():
            if set2.get(key):
                result.put(key)
        return result

    def union(self, set2):
        result = PowerSet()
        for key in self.items.keys():
            result.put(key)
        for key in set2.items.keys():
            result.put(key)
        return result

    def difference(self, set2):
        result = PowerSet()
        for key in self.items.keys():
            if not set2.get(key):
                result.put(key)
        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False
