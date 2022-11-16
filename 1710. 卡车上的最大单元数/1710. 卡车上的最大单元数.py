class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 只是箱子数量受限制，所以无脑搬最大的箱子就行了
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        res = 0
        for n,c in boxTypes:
            if n>truckSize:
                return res+truckSize*c
            else:
                res += n*c
            truckSize -= n
        return res