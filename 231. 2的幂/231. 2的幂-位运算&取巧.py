class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 这题本意当然是位运算
        # 2的幂在二进制中有且仅有一个1

        # 位运算方法1
        # n&(n-1)把n最低位的1移除，如果n>0且移除后结果为0，则是2的幂
        # return n>0 and n&(n-1)==0

        # 位运算方法2
        # 补码表示的负数计算方法：按位取反后+1
        # n&(-n)获得最低位的1，对于仅有一个1的2的幂，结果等于其自身
        #return n>0 and n&(-n)==n

        # 取巧方法
        # 在本题中最大的2的幂为2^30
        # 只要比较2^30是否能除尽n即可
        # 1<<30的括号要加
        return n>0 and (1<<30)%n == 0

s = Solution()
print(s.isPowerOfTwo(8))