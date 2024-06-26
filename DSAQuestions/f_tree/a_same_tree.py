# https://leetcode.com/problems/same-tree/
from typing import Optional  # Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def dfs(node1, node2):

        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        else:
            return False

    return dfs(p, q)
