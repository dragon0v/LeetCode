class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set("qwertyuiopasdfghjklzxcvbnm")
        for c in sentence:
            if c in s:
                s.remove(c)

        return not s