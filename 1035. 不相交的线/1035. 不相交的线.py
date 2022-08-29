class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        n,m = len(nums1),len(nums2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i,n1 in enumerate(nums1):
            for j,n2 in enumerate(nums2):
                if n1==n2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        
        return dp[n][m]

# 官方dp，转化为最长公共子序列问题，关键是思路
# 1143. 最长公共子序列