# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
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


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
print(removeNthFromEnd(l1, 2))
