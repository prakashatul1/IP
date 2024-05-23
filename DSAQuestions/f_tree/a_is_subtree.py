from typing import Optional  # Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def sameTree(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2 and node1.val == node2.val:
        return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
    return False
