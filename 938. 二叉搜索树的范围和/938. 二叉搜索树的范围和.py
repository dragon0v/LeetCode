# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 深度优先搜索
        if root.val > high:
            return self.rangeSumBST(root.left,low,high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val+self.rangeSumBST(root.left, low, high)+self.rangeSumBST(root.right,low,high)
        