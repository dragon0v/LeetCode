# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hashmap = defaultdict(list)
        def dfs(node, x, y):
            if not node:
                return
            hashmap[y].append((x,node.val))
            dfs(node.left, x+1, y-1)
            dfs(node.right, x+1, y+1)
        
        dfs(root, 0, 0)
        # zip(*)是zip()的逆操作，zip(*[(1,3),(2,4)])=[(1,2),(3,4)]
        return [list(zip(*sorted(hashmap[i])))[1] for i in sorted(hashmap.keys())]


