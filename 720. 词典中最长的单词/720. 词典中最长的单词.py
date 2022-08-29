from typing import *

class Node:
    def __init__(self,root=None) -> None:
        self.val = root
        self.children = dict() # char:Node
        
    def ischild(self,c):
        return c in self.children.keys()
    
    def addchild(self,c):
        print(self.val,'->',c)
        self.children[c] = Node(c)
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res = ''
        # 字典树？
        DT = Node()
        for word in words:
            root = DT
            flag = False
            for i,c in enumerate(word):
                if root.ischild(c):
                    root = root.children[c]
                elif i==len(word)-1:
                    root.addchild(c)
                    if len(word)>len(res):
                        res = word
                else:
                    break

        return res
s = Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
print(s)