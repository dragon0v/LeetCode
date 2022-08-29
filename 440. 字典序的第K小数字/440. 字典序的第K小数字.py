# 字节最常考的题
# 照抄的
# 思路是脑子里构思一个字典树，发现对一个结点，其下有10个子节点
# 例如1下，有10,11,12,...,19
# 10下，有100,101,...,109
# 每次缩小范围
class Solution:
    def getSteps(self, cur, n):
        '''
        Get number of nodes unber the current node.

        :param cur: Current number
        :type cur: int
        :param n: The given n
        :type n: int
        '''
        steps = 0  # how many numbers to skip
        first = cur  # the left-most node
        last = cur  # the right-most node
        while first<=n:
            steps += min(last,n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1  # Recursively ranging the result.
        k -= 1
        while k:
            steps = self.getSteps(cur,n)
            if steps<=k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur