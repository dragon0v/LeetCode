class Solution:
    def minimumLength(self, s: str) -> int:
        # 模拟，递归，超时，通过99/100用例
        def trim(s):
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
                return trim(s[i:j+1]) if i<=j else 0
            
        return trim(s)
