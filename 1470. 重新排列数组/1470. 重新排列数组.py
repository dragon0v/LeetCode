class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j = 0,n
        ans = []
        for _ in range(n):
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        
        return ans
