class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = [False for _ in range(26)]
        for c in sentence:
            s[ord(c)-ord('a')] = True
        
        return all(s)