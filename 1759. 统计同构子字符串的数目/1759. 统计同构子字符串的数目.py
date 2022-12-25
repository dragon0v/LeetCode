class Solution:
    def countHomogenous(self, s: str) -> int:
        # 感觉写的不优雅
        s += '@'
        seq = []
        last = ''
        cc = 0
        for c in s:
            if last=='':
                last=c
                cc += 1
            elif c==last:
                cc+=1
            else:
                seq.append(cc)
                cc = 1
                last = c
        
        return sum(x*(x+1)//2 for x in seq) % (10**9+7)
        