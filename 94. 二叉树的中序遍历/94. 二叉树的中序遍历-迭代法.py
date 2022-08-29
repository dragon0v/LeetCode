# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        # 迭代法
        # 属于递归法的优化，使用栈
        # 从根节点开始找二叉树的最左节点，将走过的节点保存在一个栈中，找到最左节点后访问
        # 对于每个节点来说，它都是以自己为根的子树的根节点，访问完之后就可以转到右儿子上了。
        ret = []
        if root == None:
            return ret
        cur = root
        stack = []
        while stack!=[] or cur != None:
            # 把走过的结点放在栈中
            while cur!= None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop(-1)
            ret.append(cur.val)
            cur = cur.right
        
        return ret

        
# 时间空间都是On

# https://blog.csdn.net/u012877472/article/details/49401751