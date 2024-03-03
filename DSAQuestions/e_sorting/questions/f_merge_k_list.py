"""
Asymptotic complexity in terms of total length of all given linked lists `n` and `k`:
* Time: O(n * log(k)).
* Auxiliary space: O(k).
* Total space: O(n + k).
"""

import heapq


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


def merge_k_lists(lists):
    if not lists:
        return None
    # Create a dummy node to simplify the code
    dummy = LinkedListNode(-1)
    tail = dummy

    pq = []  # Priority queue using a list

    for i, node in enumerate(lists):
        if node:
            pq.append((node.value, i, node))

    heapq.heapify(pq)  # Convert the list to a min-heap

    while pq:
        min_value, min_index, min_node = heapq.heappop(pq)

        # Append the minimum value to the result linked list
        tail.next = min_node
        tail = tail.next

        # Move the pointer of the list with the minimum value
        if min_node.next:
            heapq.heappush(pq, (min_node.next.value, min_index, min_node.next))

    return linked_list_to_list(dummy.next)


def lists_to_linked_lists(input_lists):
    linked_lists = []
    for lst in input_lists:
        head = None
        tail = None
        for val in lst:
            if head is None:
                head = LinkedListNode(val)
                tail = head
            else:
                tail.next = LinkedListNode(val)
                tail = tail.next
        linked_lists.append(head)
    return linked_lists


# Helper function to convert a LinkedListNode into a list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


print(merge_k_lists(lists_to_linked_lists(
    [
        [1, 3, 5],
        [7],
        [3, 4]
    ]
)))
