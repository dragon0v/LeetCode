from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.l = []
        def dfs(r):
            if r.left:
                dfs(r.left)
            self.l.append(r.val)
            if r.right:
                dfs(r.right)

        dfs(root)

        i,j = 0,len(self.l)-1
        while i<j:
            if self.l[i]+self.l[j]==k:
                return True
            elif self.l[i]+self.l[j]>k:
                j -= 1
            else:
                i += 1
        return False
