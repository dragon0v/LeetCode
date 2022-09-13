class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        for i,c in enumerate(n):
            # 找最大数
            m = '0'
            for j,x in enumerate(n[i:]):
                if x>=m:
                    m=x
                    idx = j+i  # 会获得最后一个最大数的下标
                    print(idx)
            if c!=m:
                # 当前位不是最大，交换
                print(n,i,idx)
                n[i],n[idx] = n[idx],n[i]
                break
        
        return int(''.join(n))

s = Solution()
t = s.maximumSwap(98368)
print(t)