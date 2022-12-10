class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m = -1
        for s in strs:
            try:
                m = max(m,int(s))
            except:
                m = max(m,len(s))
        return m