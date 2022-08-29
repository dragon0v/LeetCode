class ProductOfNumbers:
    nums = []
    product = []
    def __init__(self):
        pass

    def add(self, num: int) -> None:
        self.nums.append(num)
        # 题目数据保证：任何时候，任一连续数字序列的乘积都在 32-bit 整数范围内，不会溢出。
        # 说明add很多是0和1，如果有32个add2，就超出范围了，所以对0和1特殊处理
        if num==0:
            # 直接把product数组前面的部分截去，如果k>len(product)就说明积肯定为0
            self.product = [0]
        elif num!=1:
            self.product = [each*num for each in self.product]
        self.product.append(num)

    def getProduct(self, k: int) -> int:
        if k <= len(self.product):
            return self.product[-k]
        return 0

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)