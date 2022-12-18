class Solution:
    def countValidWords(self, sentence: str) -> int:
        # 看似简单题，要一遍过也不容易
        def isValid(w):
            # 用默认参数的split()则不需要，用split(' ')则需要
            # if w=='':
            #     return False
            cnt = 0
            # cnt2 = 0
            for i,c in enumerate(w):

                if c in '1234567890':
                    return False
                if c=='-':
                    cnt += 1
                    if cnt>1:
                        return False
                    if i==0 or i==len(w)-1:
                        return False
                    if (w[i-1] in '-!.,') or (w[i+1] in '-!.,'):
                        return False
                if c in '!.,':
                    # 不需要，如果有多个标点那么必然有不在末尾的标点
                    # cnt2 += 1
                    # if cnt2>1:
                    #     return False
                    if i!=len(w)-1:
                        return False
            return True
        
        return sum([isValid(w) for w in sentence.split()])