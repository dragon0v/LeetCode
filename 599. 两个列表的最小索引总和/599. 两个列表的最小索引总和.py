from typing import *
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        def to_dict(li):
            d = {}
            for i,v in enumerate(li):
                d[v] = i
            return d

        d1 = to_dict(list1)
        d2 = to_dict(list2)
        k1 = d1.keys()
        k2 = d2.keys()
        ans = []
        mindist = 999999999999
        for k in k1:
            if k in k2:
                dist = d1[k] + d2[k]
                if dist < mindist:
                    mindist = dist
                    ans = [k]
                elif dist==mindist:
                    ans.append(k)
        
        return ans

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

s = Solution().findRestaurant(list1,list2)
print(s)