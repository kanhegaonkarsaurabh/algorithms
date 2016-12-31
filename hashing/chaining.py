class HashTable:

    DEFAULT_SIZE = 10
    LOAD_LIMIT = 0.5

    def __init__(self):
        self.table = [[] for i in range(self.DEFAULT_SIZE)]
        self.keys = 0

    def resize(self):
        new_size = len(self.table) * 2
        table = [[] for i in range(new_size)]
        for i in range(len(self.table)):
            for key in self.table[i]:
                index = hash(key) % len(table)
                table[index].append(key)
        self.table = table

    def insert(self, key):
        self.keys += 1
        if self.keys / len(self.table) > self.LOAD_LIMIT:
            self.resize()
        index = hash(key) % len(self.table)
        self.table[index].append(key)

    def remove(self, key):
        index = hash(key) % len(self.table)
        if key in self.table[index]:
            self.table[index].remove(key)
            self.keys -= 1

    def contains(self, key):
        index = hash(key) % len(self.table)
        return True if key in self.table[index] else False
