class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # 永远找最大，相同的时候往后比，尽快拿到更大的
        # 看起来容易但情况很多，代码不太好写
        merge = ""
        l1, l2 = len(word1), len(word2)
        i = j = 0
        while i!=l1-1 or j!=l2-1:
            if ord(word1[i])>ord(word2[j]):
                merge = merge + word1[i]
                i += 1
            elif ord(word1[i])<ord(word2[j]):
                merge = merge + word2[j]
                j += 1
            else:
                # 相同的情况
                pass
        return 