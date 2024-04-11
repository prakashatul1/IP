# https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time : O(n)
# space : O(h) ~ O(logn)
def hasPathSum(self, targetSum: int, root=None) -> bool:
    if not root:
        return False

    targetSum = targetSum - root.val

    if not root.left and not root.right:
        return targetSum == 0
    if self.hasPathSum(root.left, targetSum):
        return True
    if self.hasPathSum(root.right, targetSum):
        return True

    targetSum += root.val

    return False
