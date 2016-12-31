class HashTable:

    DEFAULT_SIZE = 10

    def __init__(self):
        self.table = [()] * self.DEFAULT_SIZE
        self.elems = 0

    def resize(self):
        table = [()] * (len(self.table) * 2)
        for i in range(len(self.table)):
            elems = list(self.table[i])
            for elem in elems:
                index = hash(elem) % len(table)
                table[index] += (elem,)
        self.table = table

    def insert(self, elem):
        self.elems += 1
        if self.elems / len(self.table) > 0.5:
            self.resize()
        index = hash(elem) % len(self.table)
        self.table[index] += (elem,)

    def remove(self, elem):
        index = hash(elem) % len(self.table)
        if elem in self.table[index]:
            self.table[index] = tuple(x for x in \
                self.table[index] if x != elem)
            self.elems -= 1

    def contains(self, elem):
        index = hash(elem) % len(self.table)
        return True if elem in self.table[index] else False
