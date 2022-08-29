class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4的幂 二进制表示有且仅有一个1且此1在偶数位
        # 在判断2的幂的基础上加入4的幂的判断即可
        # 方法1：令mask=10101010101010101010101010101010，这样如果奇数位有1则结果不为0
        return n>0 and n&(n-1)==0 and n&0xAAAAAAAA==0
        # 方法2：4的幂mod3余数为1,2的幂mod3余数为2
        return n>0 and n&(n-1)==0 and n%3==1
        # 方法3：4的幂一定是完全平方数
        return n>0 and n&(n-1)==0 and n**0.5-int(n**0.5)==0