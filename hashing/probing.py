class Empty:

    def __init__(self):
        pass

    def __repr__(self):
        return 'Empty'

class HashTable:

    DEFAULT_SIZE = 10

    def __init__(self):
        self.table = [None] * self.DEFAULT_SIZE
        self.keys = 0

    def resize(self):
        pass

    def insert(self, key):
        self.keys += 1
        # TODO: resize method
        index = hash(key) % len(self.table)
        while self.table[index] is not None and \
            type(self.table[index]) is not Empty:
            index += 1
        self.table[index] = key

    def remove(self, key):
        index = hash(key) % len(self.table)
        search = 0
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
        index = hash(key) % len(self.table)
        search = 0
        while search < len(self.table):
            slot = (index + search) % len(self.table)
            if self.table[slot] is None or \
                type(self.table[slot]) is Empty:
                return False
            if self.table[slot] == key:
                return True
            search += 1
        return False
