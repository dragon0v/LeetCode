class Solution:
    def findClosest(self, words, word1, word2) -> int:
        i,j = -1,-1
        res = 100001
        for idx,each in enumerate(words):
            print(i,j)
            if each == word1:
                i = idx
                if j!=-1:
                    # 已经找到word2了
                    res = min(res,abs(i-j))
                    j = -1
            elif each == word2:
                j = idx
                if i!=-1:
                    # 已经找到word1了
                    res = min(res,abs(i-j))
                    i = -1
        
        return res


# 如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

# TODO 时间空间垫底