class Solution:
    def subtractProductAndSum(self, n):
        #print("*".join(str(n)) , "+".join(str(n)))
        return eval("*".join(str(n))) - eval("+".join(str(n)))

s=Solution()
a=s.subtractProductAndSum(1234)
# 作者：g621
# 链接：https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/solution/yi-xing-dai-ma-jian-dan-qing-xi-by-g621-32hh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。