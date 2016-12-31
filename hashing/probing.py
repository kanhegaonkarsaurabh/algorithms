class Empty:

    def __init__(self):
        pass

    def __repr__(self):
        return 'Empty'

class HashTable:

    DEFAULT_SIZE = 10
    LOAD_LIMIT = 0.5

    def __init__(self):
        self.table = [None] * self.DEFAULT_SIZE
        self.keys = 0

    def resize(self):
        table = [None] * (len(self.table) * 2)
        for i in range(len(self.table)):
            if self.table[i] is not None and \
                type(self.table[i]) is not Empty:
                index = hash(i) % len(table)
                while table[index] is not None and \
                    type(table[index]) is not Empty:
                    index = (index + 1) % len(table)
                table[index] = self.table[i]
        self.table = table

    def insert(self, key):
        self.keys += 1
        if self.keys / len(self.table) > self.LOAD_LIMIT:
            self.resize()
        index = hash(key) % len(self.table)
        while self.table[index] is not None and \
            type(self.table[index]) is not Empty:
            index = (index + 1) % len(self.table)
        self.table[index] = key

    def remove(self, key):
        search = 0
        index = hash(key) % len(self.table)
        while search < len(self.table):
            slot = (index + search) % len(self.table)
            if self.table[slot] is None or \
                type(self.table[slot]) is Empty:
                return False
            if self.table[slot] == key:
                self.table[slot] = Empty()
                self.keys -= 1
                return True
            search += 1
        return False

    def search(self, key):
        search = 0
        index = hash(key) % len(self.table)
        while search < len(self.table):
            slot = (index + search) % len(self.table)
            if self.table[slot] is None or \
                type(self.table[slot]) is Empty:
                return False
            if self.table[slot] == key:
                return True
            search += 1
        return False
