def kthSmallest(self, root: None, k: int) -> int:
    n = 0
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right
