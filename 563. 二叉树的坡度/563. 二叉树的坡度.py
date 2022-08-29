# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root==None:
            return 0
        self.ans = 0
        self.get_sum(root)
        return self.ans
    def get_sum(self,node):
        left,right = 0,0
        if node.left:
            left += self.get_sum(node.left)
        if node.right:
            right += self.get_sum(node.right)
        self.ans += abs(right-left)
        return left+right+node.val