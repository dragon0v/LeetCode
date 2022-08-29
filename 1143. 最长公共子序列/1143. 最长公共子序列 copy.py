class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # 做完1035后再做的，似乎是完全抄了一遍
        # dp
        l1,l2 = len(text1),len(text2)
        dp = [[0]*(l2+1) for i in range(l1+1)]
        
        for i,c1 in enumerate(text1):
            for j,c2 in enumerate(text2):
                if c1==c2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

        return dp[l1][l2]