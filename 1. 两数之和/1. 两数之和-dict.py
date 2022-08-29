class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in d:
                return d[another],i
            # 巧妙之处，把值作为key，下标作为value，解决set(dict.keys)无序的问题
            d[nums[i]] = i
        
            

s = Solution().twoSum([1,3,3,3,2,4],6)
print(s)

# python in 操作在list中速度很慢，在set和dict中速度很快，二者相差10000倍
# 这里很巧妙，因为要找的另一个数一定在当前数之后，所以就可以在迭代中建立dict

# 相对于1年前的朴素版，速度从800ms -> 36ms，内存增加1M
