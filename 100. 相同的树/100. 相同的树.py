# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(r,nodes):
            if r==None:
                nodes.append(1203917247)
                return
            nodes.append(r.val)
            dfs(r.left,nodes)
            dfs(r.right,nodes)
            return nodes
        
        return (dfs(p,[])) == (dfs(q,[]))