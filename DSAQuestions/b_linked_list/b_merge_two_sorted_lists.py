# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.

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


def mergeTwoLists(list1, list2):
    head = ListNode()
    curr = head

    while list1 and list2:

        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 or list2

    return head.next


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
l2 = ListNode(1, None)

print(mergeTwoLists(l1, l2))
