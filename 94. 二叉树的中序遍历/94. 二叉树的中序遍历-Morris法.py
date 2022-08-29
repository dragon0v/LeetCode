# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        # Morris法
        # 将所有右儿子为NULL的节点的右儿子指向后继节点
        # （对于右儿子不为空的节点，右儿子就是接下来要访问的节点）
        # 这样，对于任意一个节点，当访问完它后，它的右儿子已经指向了下一个该访问的节点。对于最右节点，不需要进行这样的操作。
        # 注意，这样的操作是在遍历的时候完成的，完成访问节点后会把树还原
        ret = []
        if root == None:
            return ret
        
        cur = root
        pre = None
        while cur:
            # 当前为最左结点
            if cur.left == None:
                ret.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left

            # TODO


        return ret

        
# 时间空间都是On

# https://blog.csdn.net/u012877472/article/details/49401751