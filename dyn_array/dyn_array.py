import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = self.min_cap
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self._extend()
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self._extend()
        for j in reversed(range(i, self.count)):
            self.array[j + 1] = self.array[j]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1
        self._shrink_if_needed()

    min_fill = 0.5
    min_cap = 16
    extend_factor = 2
    shrink_factor = 1/1.5
    
    def _extend(self):
        new_size = int(self.extend_factor * self.capacity)
        self.resize(new_size)

    def _shrink_if_needed(self):
        if (self.capacity == self.min_cap) or \
            (self.count >= self.min_fill * self.capacity):
            return
        new_size = int(self.shrink_factor * self.capacity)
        if new_size < self.min_cap:
            new_size = self.min_cap
        self.resize(new_size)
