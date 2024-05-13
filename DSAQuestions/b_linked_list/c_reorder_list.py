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


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    prev = None
    slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    print(head)


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
print(reorderList(l1))
