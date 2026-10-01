class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        h = self.hash(key)
        if h not in self.collection:
            self.collection[h] = {}
        self.collection[h][key] = value

    def remove(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            del self.collection[h][key]

    def lookup(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            return self.collection[h][key]
        return None
    