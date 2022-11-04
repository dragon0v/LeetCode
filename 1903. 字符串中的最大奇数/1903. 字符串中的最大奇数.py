class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)):
            if num[len(num)-1-i] in '13579':
                return num[:len(num)-i]
        return ''