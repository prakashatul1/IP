# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseList(head):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reverseListRecursive(head):
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None
    return newHead


node1 = Node(1)
node1.next = Node(2)
node1.next.next = Node(3)
node1.next.next.next = Node(4)

result = reverseListRecursive(node1)
print(result.data)


