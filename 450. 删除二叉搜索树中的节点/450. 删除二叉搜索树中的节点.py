from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None: return root
        def leftmost(node):
            while node.left != None:
                node = node.left
            return node

        last = crt = root
        if root.val == key:
            leftmost(crt.right).left = crt.left
            return crt.right

        while crt:
            if crt.val==key:
                # 情况1：无子树，直接删除此节点
                if not crt.left and not crt.right:
                    if last.val>crt.val:
                        last.left = None
                    else:
                        last.right = None
                    return root
                # 情况2：子树只有一边，直接跳过此结点
                if not crt.left or not crt.right:
                    if last.val>crt.val:
                        last.left = crt.left if crt.left else crt.right
                    else:
                        last.right = crt.left if crt.left else crt.right
                    return root
                # 情况3：子树两边都有，把crt右结点的最左结点连到crt的左节点，返回右节点
                else:
                    leftmost(crt.right).left = crt.left
                    if last.val>crt.val:
                        last.left = crt.right
                    else:
                        last.right = crt.right
                    return root

            elif crt.val > key:
                last = crt
                crt = crt.left
            else:
                last = crt
                crt = crt.right
        # 不在树中的情况
        return root

