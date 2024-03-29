import collections


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []
    q = collections.deque([root])

    while q:
        rightSide = None
        qlen = len(q)

        for i in range(qlen):

            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)

        if rightSide:
            res.append(rightSide.val)

    return res