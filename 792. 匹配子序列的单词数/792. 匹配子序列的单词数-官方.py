from typing import *
class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in xrange(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/number-of-matching-subsequences/solution/pi-pei-zi-xu-lie-de-dan-ci-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
s = Solution().numMatchingSubseq('abcde',["a","bbbbb","acd","ace"])
print(s)