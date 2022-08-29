class Solution:
    def countNicePairs(self, nums) -> int:
        revs = []
        ans = 0
        for each in nums:
            revs.append(int(str(each)[::-1])-each)
        print(revs)
        
        c = Counter(revs)
        print(c)
        for each in c.values():
            ans += each*(each-1)//2
            
        
        
        
        return ans % (10**9+7)