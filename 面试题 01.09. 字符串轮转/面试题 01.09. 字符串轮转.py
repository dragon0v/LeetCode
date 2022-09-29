class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        # 属于一个小窍门
        s3 = s2*2
        return s1 in s3 and len(s1)==len(s2)