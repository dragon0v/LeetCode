from typing import *
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        self.res = []
        def dfs(root):
            self.res.append(root.val)
            if root.children:
                for c in root.children:
                    dfs(c)
        dfs(root)
        return self.res

# 63%, 54%
s = Solution()
print(s)