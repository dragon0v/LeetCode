# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList:'[NestedInteger]'):
        # 过程类似dfs
        self.res = []
        nl = nestedList
        def dfs(nl):
            for each in nl:
                if each.isInteger():
                    self.res.append(each.getInteger())
                else:
                    dfs(each.getList())
        dfs(nl)
        
    def next(self) -> int:
        return self.res.pop(0)

    
    def hasNext(self) -> bool:
        return len(self.res)>0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# TODO 这个题给了next和hasNext，在这个解里没啥用，可能有更适合的解法
# 优化思路：用栈维护dfs中经过的所有结点，代替递归