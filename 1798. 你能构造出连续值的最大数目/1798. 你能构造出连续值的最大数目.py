class Solution:
    def getMaximumConsecutive(self, coins) -> int:
        coins.sort()
        sum = 1
        for c in coins:
            if c > sum:
                return sum
            sum += c

        return sum

s = Solution()
t = s.getMaximumConsecutive([1,1,1,4])
print(t)

# 考察思维，数学题
# 思路：取数字一定是从小开始取的，
# 如果当前数字大于之前的和+1（这里sum是因为sum初值为1），
# 则此数字和之后的数字必不能贡献