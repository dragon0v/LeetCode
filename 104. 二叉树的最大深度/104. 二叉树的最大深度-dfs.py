# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.res = -1
        def dfs(r,d):
            if r.left==None and r.right==None:
                self.res = max(d,self.res)
            if r.left:
                dfs(r.left,d+1)
            if r.right:
                dfs(r.right,d+1)
        
        dfs(root,1)
        return self.res