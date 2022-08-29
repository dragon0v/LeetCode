# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 0
        
        while 1:
            k = (i+n)//2
            print(k)
            if isBadVersion(k):
                if not isBadVersion(k-1):
                    return k
                else:
                    n = k-1
            elif not isBadVersion(k):
                if isBadVersion(k+1):
                    return k+1
                else:
                    i = k+1

N = 2126753390
BAD = 1702766719
def isBadVersion(k):
    if k >= BAD:
        return True
    return False

s = Solution().firstBadVersion(N)
print(s)