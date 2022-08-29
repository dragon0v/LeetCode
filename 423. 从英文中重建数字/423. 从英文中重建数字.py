from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        # one two three four five
        # six seven eight nine zero
        # x z g w u
        '''
        可以发现z, w, u, x, g 都只在一个数字中，即 0,2,4,6,8 中出现。
        因此我们可以使用一个哈希表统计每个字母出现的次数，那么z, w, u, x, g 出现的次数，即分别为0,2,4,6,8 出现的次数。
        随后我们可以注意那些只在两个数字中出现的字符：
        h 只在 3,8 中出现。由于我们已经知道了 8 出现的次数，因此可以计算出 3 出现的次数。
        f 只在 4,5 中出现。由于我们已经知道了 4 出现的次数，因此可以计算出 5 出现的次数。
        s 只在 6,7 中出现。由于我们已经知道了 6 出现的次数，因此可以计算出 7 出现的次数。
        此时，我们还剩下 11 和 99 的出现次数没有求出：

        o 只在 0,1,2,4 中出现，由于我们已经知道了 0,2,4 出现的次数，因此可以计算出 1 出现的次数。
        最后的 9 就可以通过 n, i, e 中的任一字符计算得到了。这里推荐使用i 进行计算，因为n 在9中出现了2次, e 在3 中出现了 2 次，容易在计算中遗漏。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/solution/cong-ying-wen-zhong-zhong-jian-shu-zi-by-9g1r/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        count = [0 for _ in range(10)]
        d = Counter(s)
        # count 02468
        for c,n in zip('xzgwu',[6,0,8,2,4]):
            count[n] = d[c]          
        # count 357
        for c,n,t in zip('hfs',[3,5,7],[8,4,6]):
            count[n] = d[c] - count[t]  
        # count 19
        count[1] = d["o"] - count[0] - count[2] - count[4]
        count[9] = d["i"] - count[5] - count[6] - count[8]
        
        res = ''
        for i,v in enumerate(count):
            if v>0:
                res += str(i)*v
        return res
                
        
s = Solution().originalDigits("fviefuro")
print(s)