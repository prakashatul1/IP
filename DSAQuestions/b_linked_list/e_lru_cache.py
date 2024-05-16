class Node:

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.key},{self.val}"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # left LRU, right most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # from left
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # from right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            print(self.cache)
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        print(self.right.prev)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        print(self.cache)


lru = LRUCache(3)

# Test inserting elements
lru.put(1, 1)  # cache: {1}
lru.put(2, 2)  # cache: {1, 2}
lru.put(3, 3)  # cache: {1, 2, 3}
print(lru.get(1))  # access 1, cache should now be {2, 3, 1}
lru.put(4, 4)  # evicts key 2, cache should now be {3, 1, 4}

# Verify that the least recently used key '2' was evicted
assert lru.get(2) == -1, "Key 2 should be evicted; expected -1"

# Access key 1 to make it the most recently used
assert lru.get(1) == 1, "Key 1 should be available; expected 1"
lru.put(5, 5)  # evicts key 3, cache should now be {1, 4, 5}

# Verify new inserts and evictions
assert lru.get(3) == -1, "Key 3 should be evicted; expected -1"
assert lru.get(4) == 4, "Key 4 should be available; expected 4"
assert lru.get(5) == 5, "Key 5 should be available; expected 5"

print("All tests passed!")
