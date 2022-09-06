# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # 遍历时给结点标上深度和列位置
        cols = defaultdict(list)  # col:[[depth,val],...]
        def dfs(node,depth,col):
            if node==None:
                return 
            cols[col].append([depth,node.val])
            dfs(node.left, depth+1, col-1)
            dfs(node.right, depth+1, col+1)
        
        dfs(root,0,0)
        print(cols)
        # 根据储存的信息还原答案
        k = sorted(cols.keys())
        ans = []
        for col in k:
            dv = cols[col]  # [[depth,val],...]
            #######
            # 根据深度排序
            # 深度相同则按结点的值从小到大进行排序。
            # 学到了！sort 的key可以使用返回元组的lambda函数来实现基于主要/次要条件的排序
            dv.sort(key=lambda x:(x[0],x[1]))
            # sorted也同样可以 dv = sorted(dv,key=lambda x:(x[0],x[1]))
            #######
            print(dv)
            ans.append([t[1] for t in dv])
        return ans

