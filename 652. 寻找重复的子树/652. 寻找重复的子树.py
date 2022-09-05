from collections import defaultdict
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # 序列化+先序遍历
        d = defaultdict(int)  # 
        res = []

        def dfs(root):
            if root==None:
                return ''
            s = str(root.val)+'_'+dfs(root.left)+'_'+dfs(root.right)
            d[s] += 1
            if d[s] == 2:
                res.append(root)
            
            return s
        
        dfs(root)
        return res
