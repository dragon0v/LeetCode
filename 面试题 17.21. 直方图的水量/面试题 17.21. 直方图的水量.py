class Solution:
    def trap(self, height) -> int:
        area = 0
        n = len(height)
        # 找到最高的和其左右最高的，然后找到一个长方形，减去其中所有的柱子长度
        def findmax(start=0,end=n):
            maxh = -1 # 最大的柱子高度
            maxi = start # 最高的柱子下标
            for i,v in enumerate(height[start:end]):
                if v > maxh:
                    maxh = v
                    maxi = i
            return maxh,maxi
        
        
        
        while maxlh>0 or maxrh<n-1:
            # 全局最大
            maxh,maxi = findmax()
            # 左边最大
            maxlh, maxli = findmax(0,maxi)
            # 右边最大
            maxrh, maxri = findmax(maxi+1,n)
            
            # 如果找不到值为-1，目前暂未考虑
            area += maxlh*(maxi-maxli)
            area += maxrh*(maxri-maxi)
        
        
        
        
        
        area -= sum(height)
        return area
        
s = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(s)
            
        
        
        
        
        
        
        
        
        
        