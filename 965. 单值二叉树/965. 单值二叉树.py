# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        v = root.val
        self.flag = True # 
        def dfs(r):
            if r.val != v:
                self.flag = False # 若不使用self，此处修改的flag是dfs函数内的局部变量
            if r.left:
                dfs(r.left)
            if r.right:
                dfs(r.right)
        dfs(root)
        return self.flag
        