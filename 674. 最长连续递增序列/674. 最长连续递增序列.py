class Solution:
	def findLengthOfLCIS(self, nums) -> int:
		a = len(nums)
		# 海象表达式要加括号，否则a为True
		if a <=1:
			return a
		j = 1
		maxlen = 1
		t = 1
		while j < a:
			if nums[j] > nums[j-1]:
				t += 1
				# j += 1
			else:
				maxlen = max(maxlen,t)
				if maxlen > a<<1 :
					return maxlen
				t = 1
			j+=1

		return max(maxlen,t) # 最后一次更新maxlen
		
# 这题并不需要滑动窗口，直接循环就行了。。。
# 但细节还是听多的，错了两次
# 重复利用len(nums)确实可以加速的？怀疑

s = Solution()
t = s.findLengthOfLCIS([3,2,1])
print(t)

