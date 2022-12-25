class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # 周赛暴力版
        n = len(words)
        res = n+100
        for i in range(n):
            if words[(startIndex+i)%n] == target:
                res = min(res,i)
            if words[(startIndex-i)%n] == target:
                res = min(res,i)

        return res if res<n+10 else -1