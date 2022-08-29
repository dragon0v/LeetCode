from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 向下一层就将原结果*2
        nums = []
        def dfs(root,crt):
            if not root.left and not root.right:
                nums.append(crt)
            if root.left:
                crtl=crt*2+root.left.val
                dfs(root.left,crtl)
            if root.right:
                crtr=crt*2+root.right.val
                dfs(root.right,crtr)
            
        dfs(root,root.val)

        return sum(nums)

# TODO递归转循环