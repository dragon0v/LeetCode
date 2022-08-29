# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        # 递归法
        # 这是思路最简单的方法，容易想到并且容易实现。
        # 递归的终止条件是当前节点是否为空。
        # 首先递归调用遍历左子树，然后访问当前节点，最后递归调用右子树。
        def traverse(ret,root):
            if root == None:
                return
            traverse(ret,root.left)
            ret.append(root.val)
            traverse(ret,root.right)
            
        ret = []
        if root == None:
            return ret
        traverse(ret,root)
        return ret
        





# https://blog.csdn.net/u012877472/article/details/49401751