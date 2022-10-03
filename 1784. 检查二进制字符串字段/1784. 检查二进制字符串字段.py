class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not ('10' in s and '01' in s)  # 由于不会有前导0，所以10的判断可以省略
        '''
        true共三种情况：都不会出现01
        1. 全0
        2. 只有一个连续的1：111111000000
        3. 全1
        false：都会出现01
        1. 1000001
        2. 10000100
        '''
        return '01' not in s