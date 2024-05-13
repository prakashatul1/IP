# https://leetcode.com/problems/reverse-linked-list/description/
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


def reverseList(head):
    if not head or not head.next:
        return head

    first, second = None, head

    while second:
        nxt = second.next
        second.next = first
        first = second
        second = nxt
    return first


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
print(reverseList(l1))
