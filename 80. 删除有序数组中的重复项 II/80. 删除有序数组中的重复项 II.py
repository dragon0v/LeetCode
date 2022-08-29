class Solution:
    def removeDuplicates(self, nums) -> int:
        # nums.sort()
        c = 1
        last = None
        i = 0
        while i < len(nums):
            if last!=None:
                if nums[i] == last:
                    c += 1
                    if c > 2:
                        # nums.pop(i)
                        del nums[i]
                        i -= 1
                else:
                    c = 1
            
            last = nums[i]
            i += 1
        
        return len(nums)