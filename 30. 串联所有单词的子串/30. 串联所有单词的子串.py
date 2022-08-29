class Solution:
    def findSubstring(self, s: str, words):
        words_num = [] # 存放每个单词在words里的下表，不存在的为-1
        n = len(words)
        step = len(words[0])
        res = []
        for i in range(len(s)//step):
            word = s[i*step:(i+1)*step]
            try:
                words_num.append(words.index(word))
            except ValueError:
                words_num.append(-1)
        print(words_num)
        
        ref = []
        exist = []
        x = 0
        for each in words:
            if each not in exist:
                exist.append(each)
                ref.append(x)
                x += 1
            else:
                ref.append(exist.index(each))
        ref.sort()
        print(ref)
        
        for j in range(len(s)//step-n+1):
            t = words_num[j:j+n]
            t = t[:]
            t.sort()
            if t == ref:
                res.append(j*step)
                
        return res
    
# "wordgoodgoodgoodbestword",["word","good","best","good"]
s = Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"])
print('ans',s)

# 做错了，这种解法要求words无重复 - 已修正
# 还是错了，"xfoobarxx",['foo','bar']