from DSAQuestions.f_tree.bst import TreeNode


def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not preorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid + 1])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root
