class Solution:
    def candy(self, ratings) -> int:
        # 困难题，贪心
        # 解法思路来自LeetCode101.pdf
        # 知道解法感觉只是中等题

        # 将所有人的糖果初始化为1
        candy = [1 for _ in ratings]
        # 进行两次遍历，
        # 从左往右一次，如果右孩子比左孩子评分高，则把右边孩子糖果数更新为左边+1
        # 从右往左一次，如果左孩子比右孩子评分高，且左孩子当前糖果数不大于右边孩子的糖果数，则把左边孩子糖果数更新为右边+1
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = candy[i] + 1
        for j in range(len(ratings)-1,0,-1):
            if ratings[j-1] > ratings[j] and candy[j-1]<=candy[j]:
                candy[j-1] = candy[j] + 1
        print(candy)
        return sum(candy)

s = Solution()
t = s.candy([1,3,2,2,1])
print(t)



