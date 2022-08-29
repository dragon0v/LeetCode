class Solution:
    def isPalindrome(self, x: int) -> bool:
        def f(x):
            res = 0
            while 1:
                a = x%10 #个位
                res = res*10 + a
                x = x//10
                if(x==0):
                    break
            return res
        if(x<0):
            return False
        else:
            return x==f(x)

# 这里本来有个陷阱，翻转后可能会超出2^31-1
# 但是其实溢出不影响，因为这个数原来肯定不溢出，但是翻转后溢出，所以必然不是回文数
# 所以官方的解法是翻转一半和剩下的比
# 还有一个陷阱是除了0以外以0结尾的必不是回文数，但这也是不影响的