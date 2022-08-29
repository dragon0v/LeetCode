class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==1:
            return [nums[0]**2]
        # 同样是双指针，将ij放在数组两边
        i,j,p = 0,n-1,n-1
        # 然后ij往中间走，把大的平方数放res最前面
        res = [0] * n
        while i<=j:
            s1 = nums[i]**2
            s2 = nums[j]**2
            if  s1>s2:
                # res.insert(0, s1)
                # res = [s1] + res
                res[p] = s1
                i += 1
            else:
                # res.insert(0, s2)
                res[p] = s2
                j -= 1
            p -= 1   
        return res

# 发现比第一种还慢两三倍，很有可能是insert函数的问题
# 改成res = [s1] + res又更慢两三倍
# 改成固定res=[0,0,0,...]再插入，时间和第一种相同
