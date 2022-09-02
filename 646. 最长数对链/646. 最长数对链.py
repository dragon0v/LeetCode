class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 贪心，优先选pair[1]小的
        pairs.sort(key=lambda x:x[1])
        print(pairs)

        crt = pairs[0]
        l = 1
        for p in pairs:
            if p[0]>crt[1]:
                crt = p
                l += 1
        
        return l