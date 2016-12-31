class HashTable:

    DEFAULT_SIZE = 10

    def __init__(self):
        self.table = [[] for i in range(self.DEFAULT_SIZE)]
        self.elems = 0

    def resize(self):
        new_size = len(self.table) * 2
        table = [[] for i in range(new_size)]
        for i in range(len(self.table)):
            for elem in self.table[i]:
                index = hash(elem) % len(table)
                table[index].append(index)
        self.table = table

    def insert(self, elem):
        self.elems += 1
        if self.elems / len(self.table) > 0.5:
            self.resize()
        index = hash(elem) % len(self.table)
        self.table[index].append(elem)

    def remove(self, elem):
        index = hash(elem) % len(self.table)
        if elem in self.table[index]:
            self.table[index].remove(elem)
            self.elems -= 1

    def contains(self, elem):
        index = hash(elem) % len(self.table)
        return True if elem in self.table[index] else False
