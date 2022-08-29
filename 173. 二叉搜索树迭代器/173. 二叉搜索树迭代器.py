# Definition for a binary tree node.
from _typeshed import NoneType


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# 中序遍历可参考 94. 二叉树的中序遍历
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.vals = []

        # 迭代法进行中序遍历
        cur = root
        stack = []
        while stack!=[] or cur != None:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop(-1)
            self.vals.append(cur.val)
            cur = cur.right

    def next(self) -> int:
        return self.vals.pop(0)

    def hasNext(self) -> bool:
        return self.vals != []



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()