class Solution:
    def numDecodings(self, s: str) -> int:
        # dp 递归理论可行，但复杂度达不到要求，所以递归->递推=dp
        # 设f(i)表示前i个字符的解码方法数
        # 每次到达f(i)，可以是i-1后的一个字符，也可能是i-2后的两个字符
        # 一个字符：c!=0，f(i)=f(i-1),其中s[i]!=0
        # 两个字符：10<=c1c2<=26。f(i)=f(i-2),其中10<=s[i-2:i]<=26,i>=2
        # 推理过程是关键
        
        n = len(s)
        # f(0) = 1，空字符串有一种翻译
        # a=f(i-2) b=f(i-1) c=f(i)
        a,b,c = 0,1,0
        for i in range(1,n+1):
            c = 0
            # 两种到达i的方式，相加就是到达i的全部可能情况
            if s[i-1]!='0':
                c+=b
            if i>1 and s[i-2]!='0' and int(s[i-2:i])<=26:
                c+=a
            a,b = b,c
        return c
        
        

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。