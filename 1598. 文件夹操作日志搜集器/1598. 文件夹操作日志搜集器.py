class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for l in logs:
            if l=='../':
                level = max(level-1,0)
            elif l=='./':
                pass
            else:
                level += 1
        
        return level