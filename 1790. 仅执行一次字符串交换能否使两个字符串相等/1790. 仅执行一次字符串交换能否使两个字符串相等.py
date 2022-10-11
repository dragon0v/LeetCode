class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 针对竞赛等的快速做法，费了很多不必要的时间
        return Counter(s1)==Counter(s2) and sum(c1!=c2 for c1,c2 in zip(s1,s2))<3