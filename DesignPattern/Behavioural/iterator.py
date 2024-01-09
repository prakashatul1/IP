class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    # Define Iterator
    def __iter__(self):
        self.cur = self.head
        return self

    # Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration
# Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
myList = LinkedList(head)

# Iterate through LinkedList
for n in myList:
    print(n)


class SocialMediaFeed:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def __iter__(self):
        return FeedIterator(self.posts)

class FeedIterator:
    def __init__(self, posts):
        self.posts = posts
        self.index = 0

    def __next__(self):
        if self.index < len(self.posts):
            post = self.posts[self.index]
            self.index += 1
            return post
        raise StopIteration

feed = SocialMediaFeed()
feed.add_post("Post 1: Hello, world!")
feed.add_post("Post 2: Having a great day!")
feed.add_post("Post 3: Just learned about iterators in Python!")

for post in feed:
    print(post)
