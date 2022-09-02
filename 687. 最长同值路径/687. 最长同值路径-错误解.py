# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 错误解，要求是路径，此解是所有同值连线的长度  [1,null,1,1,1,1,1,1]
        self.ans = 0
        self.crt = 0
        self.dfs(root,None)

        return self.ans

    def dfs(self,r,last):
        print('dfs',r,last)
        if r==None:
            self.ans = max(self.ans,self.crt)
            return
        if r.val==last:
            self.crt += 1
            self.ans = max(self.ans,self.crt)
        else:
            self.crt = 0
        
        self.dfs(r.left, r.val)
        self.dfs(r.right, r.val)

        self.ans = max(self.ans,self.crt)


        

