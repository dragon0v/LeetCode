
# 思路：位置i是否翻转，与他前面K-1个元素的翻转次数有关：共翻转偶数次则不变，奇数次则变



class Solution():
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = []
        res = 0
        for i in range(N):
            if que and i >= que[0] + K: # 判断队列存在，为首先几次操作的特例
                que.pop(0)
            if len(que) % 2 == A[i]: #需要翻转第i个元素
                if i +  K > N:
                    return -1
                que.append(i)
                res += 1
        return res

# 作者：fuxuemingzhu
# 链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/hua-dong-chuang-kou-shi-ben-ti-zui-rong-z403l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
s = Solution()
r = s.minKBitFlips([0,0,0,1,0,1,1,0],3)
print(r)
