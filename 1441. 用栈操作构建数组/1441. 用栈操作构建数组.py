class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        n = target[-1]
        ans = []
        now = 1
        for t in target:
            if t!=now:
                for i in range(t-now):
                    ans.append("Push")
                    ans.append("Pop")
            ans.append("Push")  # push当前数字
            now = t+1
        
        return ans