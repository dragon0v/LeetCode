from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 暴力循环
        res = []
        for v in nums1:
            flag = False
            for each in nums2:
                if flag and each>v:
                    res.append(each)
                    flag = False  # 一个flag同时表示了元素和更大值的获得情况
                    break
                if each == v:
                    flag = True
            if flag:
                res.append(-1)
        
        return res

s = Solution()
t = s.nextGreaterElement([4,1,2],[1,3,4,2])
print(t)