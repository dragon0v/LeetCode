class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # 零的个数只和因式分解后5的个数有关，有多少5就有多少0
        # 所以有k个0的个数一定是0或5
        # 没有k个0的情况：k=4:20~24,k=6:25~29,无k=5
        # 所以当每出现一个5^2,5^3,5^4就会相应出现1,2,3个没0的情况
        # 朴素思想是枚举有多少个满足条件的k
        # 按这种方法复杂度太高，肯定不行
        return 'xxxx'
        ks = set()  # 所有可能的k值
        for x in range(10**9*5):
            ks.add(sum(x//(5**t) for t in range(13)))  # x!末尾0的个数，见LC172
        # print(max(ks))
        return 5 if k in ks else 0