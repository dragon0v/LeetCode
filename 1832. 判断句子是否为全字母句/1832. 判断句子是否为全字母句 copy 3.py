class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 最先想到的方法counter其实本质就是set，用set会更快
        return len(set(sentence))==26