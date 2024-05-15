# https://leetcode.com/problems/linked-list-cycle/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        result = []

        while node:
            result.append(node.val)
            temp = node
            node = temp.next

        return str(result)


def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next = l2.next

print(hasCycle(l1))
print(hasCycle(l2))


