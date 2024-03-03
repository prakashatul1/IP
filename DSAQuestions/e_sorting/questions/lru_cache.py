class LRUCache:

    def __init__(self):
        self.hashmap = {}
        pass

    def get(self, key):
        if key not in self.hashmap:
            return -1

        node = self.hashmap.get(key)
