class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # 看copy版的方法，sum+startswith
        return len(list(filter(lambda s:s[:len(pref)]==pref, words)))
        return sum(word.find(pref)==0 for word in words)