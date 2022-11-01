class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # 双指针
        # p1p2表示遍历到了w1和w2的第p个单词，ij表示遍历到了w[p]的第i位
        p1 = p2 = i = j = 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1][i] != word2[p2][j]:
                return False
            i += 1
            if i == len(word1[p1]):
                p1 += 1
                i = 0
            j += 1
            if j == len(word2[p2]):
                p2 += 1
                j = 0
        return p1 == len(word1) and p2 == len(word2)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/check-if-two-string-arrays-are-equivalent/solutions/1938926/jian-cha-liang-ge-zi-fu-chuan-shu-zu-shi-9iuo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。