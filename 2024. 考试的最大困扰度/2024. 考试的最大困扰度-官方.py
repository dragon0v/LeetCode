class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0, 0, 0  # sum表示当前范围内修改的数量
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam/solution/kao-shi-de-zui-da-kun-rao-du-by-leetcode-qub5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 加餐：
# 424. 替换后的最长重复字符
# 1004. 最大连续1的个数 III
# 1208. 尽可能使字符串相等