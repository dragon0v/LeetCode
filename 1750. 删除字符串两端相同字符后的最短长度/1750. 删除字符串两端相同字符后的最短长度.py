class Solution:
    def minimumLength(self, s: str) -> int:
        # 模拟
        while len(s)>0:
            n = len(s)
            if n==1:
                return 1
            if s[0] != s[-1]:
                return len(s)
            else:
                c = s[0]
                i,j = 0,n-1
                while i<n-1 and s[i]==c:
                    i += 1
                while j>0 and s[j]==c:
                    j -= 1
                if i<=j:
                    s = s[i:j+1]
                else:
                    # i>j说明剩下的全是一样的，全部消掉返回0
                    return 0
            
