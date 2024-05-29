
class Node:

    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f"{self.val}"


class LRU:

    def __init__(self, capacity) -> None:
        self.capacity = capacity if capacity > 0 else 0
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return None

    def put(self, key, value):

        if self.capacity:

            if key in self.cache:
                self.remove(self.cache[key])

            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove(lru)

                del self.cache[lru.key]


# l1 = LRU(3)
# l1.put("one", "one")
# assert l1.get("one") == "one"
# l1.put("two", "two")
# assert l1.get("two") == "two"
# l1.put("three", "three")
# assert l1.get("three") == "three"
# l1.put("four", "four")
# assert l1.get("four") == "four"
# assert l1.get("one") == None

l1 = LRU(3)
l1.put("one", "one")
assert l1.get("one") == "one"
l1.put("two", "two")
assert l1.get("two") == "two"
l1.put("three", "three")
l1.get("one")
l1.put("four", "four")
print(l1.cache)

# l1 = LRU(3)
# l1.put("one", "one")
# l1.put("two", "two")
# l1.put("three", "three")
# l1.put("four", "four")
# print(l1.cache)

# l1 = LRU(3)
# l1.put("one", "one")
# l1.put("two", "two")
# l1.put("three", "three")
# l1.put("four", "four")
# l1.put("one", "1")
# print(l1.cache)

# l1 = LRU(3)
# l1.put("one", "one")
# l1.put("two", "two")
# l1.put("three", "three")
# l1.put("one", "1")
# l1.put("seven", "seven")
# print(l1.cache)


# l1 = LRU(0)
# l1.put("one", "one")
# print(l1.get("one"))
# print(l1.cache)


