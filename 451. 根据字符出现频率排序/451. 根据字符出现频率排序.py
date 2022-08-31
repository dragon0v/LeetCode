from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # 这题的本意应该是自己写一个Counter
        c = Counter(s)
        ans = ''
        for char, freq in c.most_common():
            ans += char*freq
        
        return ans