# 想把一个数的二进制表示中最左边的1到最右边全变成1？
# （比如：0b0001001 -> 0b0001111）


def all_ones(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return x
# 想取得一个数的二进制表示中最左边的1？


def leftmost(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return x - (x >> 1)
# 这个问题只需要用上面的第一个函数。

# 比如要将0b0001001变成0b0000110?

# all_ones(0b0001001) -> 0b0001111
# 0b0001001 ^ 0b0001111 -> 0b0000110

def findComplement(num: int) -> int:
    return num ^ all_ones(num)

# 作者：sakuragi1111
# 链接：https://leetcode-cn.com/problems/number-complement/solution/python-jian-dan-yi-dong-by-sakuragi1111-fwc2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print(findComplement(3232))