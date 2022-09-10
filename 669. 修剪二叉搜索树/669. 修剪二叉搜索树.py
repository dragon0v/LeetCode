# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 注意，根节点可能会根据给定的边界发生改变。
        self.low = low
        self.high = high
        def dfs(r):
            if r==None:
                return None
            # 根节点太小，向右搜索，并修改root
            if r.val < self.low:
                return dfs(r.right)
            if r.val > self.high:
                return dfs(r.left)
            # 根节点在范围内，
            r.left = dfs(r.left)
            r.right = dfs(r.right)
            return r

        return dfs(root)