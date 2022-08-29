class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))

# 作者：swants
# 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/solution/python-fan-zhuan-zi-fu-chuan-zhong-dan-ci-si-lu-xi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 参见python学习笔记-基础-Python实现字符串反转的几种方法