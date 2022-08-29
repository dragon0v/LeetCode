# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if root == None:
            return []
        res=[]
        v=[str(root.val)]
        def backtrack(tn):
            if tn.left==None and tn.right==None:
                res.append("->".join(v))
            else:
                if tn.left != None:
                    v.append(str(tn.left.val))
                    backtrack(tn.left)
                    v.pop(-1)
                if tn.right != None:
                    v.append(str(tn.right.val))
                    backtrack(tn.right)
                    v.pop(-1)
        backtrack(root)
        return res