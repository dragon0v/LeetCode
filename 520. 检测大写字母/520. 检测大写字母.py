class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return any((word.isupper(),word.islower(),word.istitle()))