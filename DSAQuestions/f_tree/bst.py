class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root


def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def DFS(root):
    queue = []

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print('level:', level)

        for i in range(len(queue)):
            curr = queue.pop(0)
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1




root_node = TreeNode(val=27)
insert(root_node, val=30)
insert(root_node, val=22)
insert(root_node, val=24)
insert(root_node, val=17)
# remove()


inorder(root_node)
# 17, 22, 24, 27, 30
print('\n')
preorder(root_node)
# 27, 22, 17, 24, 30
print('\n')
DFS(root_node)
# 27, 22, 30, 17, 24
