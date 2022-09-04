class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # 思路：遇到子数组一般都是双指针，这里用ij维护一个区间，直接计算即可
        ans = 1
        cur = [nums[0]]
        i,j = 0,1
        while j<len(nums):
            flag = True
            for k,v in enumerate(cur):
                if v&nums[j] !=0:
                    i = i+k+1
                    ans = max(ans,len(cur))
                    if i==j:
                        j = j+1
                        cur = [nums[i]]
                    else:
                        cur = cur[k+1:]
                    
                    flag= False
                    break
            if flag:
                cur.append(nums[j])
                j += 1
                
        
        return max(ans,len(cur))
        
