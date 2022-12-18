class Solution:
    def countValidWords(self, sentence: str) -> int:
        # 看似简单题，要一遍过也不容易
        # 错误解
        def isValid(w):
            print(w)
            if w=='':
                return False
            cnt = 0
            cnt2 = 0
            for i,c in enumerate(w):
                if c in '1234567890':
                    return False
                if c=='-':
                    cnt += 1
                    if cnt>1:
                        return False
                    if i==0 or i==len(w)-1:
                        return False
                    if w[i-1] in '-!.,' or w[i-1] in '-!.,':
                        return False
                if c in '!.,':
                    cnt2 += 1
                    if cnt2>1:
                        return False
                    if i!=len(w)-1:
                        return False
            return True
        
        return sum([isValid(w) for w in sentence.split()])
                
                