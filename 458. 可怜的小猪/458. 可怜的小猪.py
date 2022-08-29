class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest//minutesToDie # 小猪可以喝水的轮数
        # 有n只猪，每次可以测试2^n桶水
        # rounds=1，经典问题，2^n >= buckets

        # 进制观念：
        # 例如round=1，则为2进制，编号为i的猪代表二进制的每一位，
        # 第n个水桶对应二进制中的每个1对应的猪喝这桶水，
        # 死掉的猪得到的二进制数字就是有毒的桶编号
        # 再例如round=2，则为3进制，编号为i的猪代表三进制的每一位，
        # 第一轮第n个水桶对应三进制中的每个1对应的猪喝这桶水，
        # 第二轮第n个水桶对应三进制中的每个2对应的猪和这桶水，
        # 两次死掉的猪分别表示对应位上的值为1或2，得到桶编号
        # 即(round+1)**n >= buckets
        for i in range(0,1000):
            if (rounds+1)**i >= buckets:
                return i
        
s = Solution().poorPigs(888,1,2)
print(s)