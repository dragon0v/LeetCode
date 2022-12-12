class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 用一个26位的二进制数字来表示集合，空间O(1)
        s = 0
        for c in sentence:
            s |= 1<<(ord(c)-ord('a'))
        return s == (1<<26) - 1