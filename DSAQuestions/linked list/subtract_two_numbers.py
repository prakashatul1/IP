# Python program to subtract smaller
# valued list from larger valued list
# and return result as a list.

# A linked List Node
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# A utility which creates Node.
def newNode(data):
    temp = Node(0)
    temp.data = data
    temp.next = None
    return temp


# A utility function to get
# length of linked list
def getLength(Node):
    size = 0

    while Node != None:
        Node = Node.next
        size = size + 1

    return size


# A Utility that padds zeros in
# front of the Node, with the
# given diff
def paddZeros(sNode, diff):
    if (sNode == None):
        return None

    zHead = newNode(0)
    diff = diff - 1
    temp = zHead
    while (diff > 0):
        diff = diff - 1
        temp.next = newNode(0)
        temp = temp.next

    temp.next = sNode
    return zHead


borrow = True


# Subtract LinkedList Helper is a
# recursive function, move till the
# last Node, and subtract the digits
# and create the Node and return the
# Node. If d1 < d2, we borrow the number
# from previous digit.
def subtractLinkedListHelper(l1, l2):
    global borrow

    if (l1 == None and
            l2 == None and not borrow):
        return None

    l3 = None
    l4 = None
    if (l1 != None):
        l3 = l1.next
    if (l2 != None):
        l4 = l2.next
    previous = subtractLinkedListHelper(l3, l4)

    d1 = l1.data
    d2 = l2.data
    sub = 0

    # If you have given the value value
    # to next digit then reduce the d1 by 1
    if (borrow):
        d1 = d1 - 1
        borrow = False

    # If d1 < d2, then borrow the number
    # from previous digit. Add 10 to d1
    # and set borrow = True
    if (d1 < d2):
        borrow = True
        d1 = d1 + 10

    # Subtract the digits
    sub = d1 - d2

    # Create a Node with sub value
    current = newNode(sub)

    # Set the Next pointer as Previous
    current.next = previous

    return current


# This API subtracts two linked lists
# and returns the linked list which
# shall have the subtracted result.
def subtractLinkedList(l1, l2):
    # Base Case.
    if (l1 == None and l2 == None):
        return None

    # In either of the case, get the
    # lengths of both
    # Linked list.
    len1 = getLength(l1)
    len2 = getLength(l2)

    lNode = None
    sNode = None

    temp1 = l1
    temp2 = l2

    # If lengths differ, calculate the
    # smaller Node and padd zeros for
    # smaller Node and ensure both larger
    # Node and smaller Node has equal length.
    if (len1 != len2):
        if (len1 > len2):
            lNode = l1
        else:
            lNode = l2

        if (len1 > len2):
            sNode = l2
        else:
            sNode = l1
        sNode = paddZeros(sNode, abs(len1 - len2))

    else:

        # If both list lengths are equal, then
        # calculate the larger and smaller list.
        # If 5-6-7 & 5-6-8 are linked list, then
        # walk through linked list at last Node
        # as 7 < 8, larger Node is 5-6-8 and
        # smaller Node is 5-6-7.
        while (l1 != None and l2 != None):
            if (l1.data != l2.data):
                if (l1.data > l2.data):
                    lNode = temp1
                else:
                    lNode = temp2

                if (l1.data > l2.data):
                    sNode = temp2
                else:
                    sNode = temp1
                break

            l1 = l1.next
            l2 = l2.next

    global borrow

    # After calculating larger and smaller
    # Node, call subtractLinkedListHelper
    # which returns the subtracted
    # linked list.
    borrow = False
    return subtractLinkedListHelper(lNode,
                                    sNode)


# A utility function to print
# linked list
def printList(Node):
    while (Node != None):
        print(Node.data,
              end=" ")
        Node = Node.next
    print(" ")


# Driver code
head1 = newNode(1)
head1.next = newNode(0)
head1.next.next = newNode(0)
head2 = newNode(1)
result = subtractLinkedList(head1, head2)
printList(result)
# This code is contributed by Arnab Kundu
