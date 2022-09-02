# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 用DFS来求过根节点的路径，左右两条路径相加就是可以不过根节点的路径(这里的不过根节点是对于整棵树而言)。
        self.ans = 0
        self.dfs(root)

        return self.ans

    def dfs(self,r):
        # print('dfs',r)
        if r==None:
            return 0
         
        left = self.dfs(r.left)  # 左子树的最长路径值，递归思想
        right = self.dfs(r.right)  

        left1 = right1 = 0  # 如果左右子树和根相连是相同数字，则左右子树最长路径数+1（和根连），否则为0
        if r.left!=None and r.left.val == r.val:
            left1 = left + 1
        if r.right!=None and r.right.val == r.val:
            right1 = right + 1

        self.ans = max(self.ans,left1+right1)
        return max(left1,right1)


        

