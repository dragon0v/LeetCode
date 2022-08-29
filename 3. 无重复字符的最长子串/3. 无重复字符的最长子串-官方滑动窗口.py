class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用集合！！！
        occ = set()
        n = len(s)
        i,j = 0,0
        ans = 0
        for i in range(n):
            while j<=n-1 and s[j] not in occ:
                occ.add(s[j])
                j += 1
            ans = max(ans,j-i)
            occ.remove(s[i])
            
        return ans
        
        

# 思路：滑动窗口，如果已经知道了某个子串符合条件，那么当左边界右移，
# 当前范围内元素均满足条件，所以只需将右边界右移，每次更新最大值
# 和官方有改动，感觉这样更直观
s = Solution().lengthOfLongestSubstring('aababbcaa')
print(s)
