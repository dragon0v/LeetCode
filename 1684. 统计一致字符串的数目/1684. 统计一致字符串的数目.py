class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        return len(list(filter(lambda w:all([c in a for c in w]), words)))