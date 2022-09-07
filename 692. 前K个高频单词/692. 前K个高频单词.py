from typing import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 题目要求相同频率按字幕序返回，这是普通counter无法做到的
        words.sort()  # 这里可以利用python字典的新特性(3.6后)，先排序，保证在字典中key是有序的
        c = Counter(words)
        freq = c.most_common(k)
        fl = [kv[0] for kv in freq]
        return fl

s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
t = s.topKFrequent(words,k)
print(t)

# 进阶：尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
# 此方法sort是nlogn，不符合