class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # 整体思路和代码结构是一样的，但是高度精练
        merge = []  # 使用list+''.join()会更快
        i, j, n, m = 0, 0, len(word1), len(word2)
        while i < n or j < m:
            if i < n and word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        return ''.join(merge)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/largest-merge-of-two-strings/solutions/2030226/gou-zao-zi-dian-xu-zui-da-de-he-bing-zi-g6az1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 还有一个后缀数组的高级解法