class Solution:
    def reformat(self, s: str) -> str:
        # 顺序遍历获得两者数量，再通过交换原地构造答案
        sumDigit = sum(c.isdigit() for c in s)
        sumAlpha = len(s) - sumDigit
        if abs(sumDigit - sumAlpha) > 1:
            return ""
        flag = sumDigit > sumAlpha  # True表示数字多于字母，则数字需在最前
        t = list(s)
        j = 1
        for i in range(0, len(t), 2):
            if t[i].isdigit() != flag:
                while t[j].isdigit() != flag:
                    j += 2
                t[i], t[j] = t[j], t[i]
        return ''.join(t)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/reformat-the-string/solution/zhong-xin-ge-shi-hua-zi-fu-chuan-by-leet-lgqx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。