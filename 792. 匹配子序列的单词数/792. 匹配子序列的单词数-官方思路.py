from typing import *
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 由于单词
        def mord(c):
            return ord(c)-ord('a')
        
        heads = [[] for _ in range(26)]
        for w in words:
            heads[mord(w[0])].append(w)
        # print(heads)
        
        # TODO 这里的代码块太丑了
        res = 0
        for c in s:
            if heads[mord(c)]!=[]:
                t = []
                for word in heads[mord(c)]:
                    if len(word)==1:
                        res += 1
                    else:
                        if word[0]==word[1]:
                            t.append(word[1:])
                        else:
                            word=word[1:]
                            heads[mord(word[0])].append(word)
                heads[mord(c)] = t
                
                
        return res
                        
                        
        
    
s = Solution().numMatchingSubseq('abcde',["a","bbbbb","acd","ace"])
print(s)