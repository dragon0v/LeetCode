class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()

        # 大小写差了32，所以在他们的二进制表示中第6位一个为1一个为0
        # print(ord('a'),ord('A'))
        # return ''.join(chr(asc|32) if 65<=(asc:=ord(c))<=90 else c for c in s)
        # 小写转大写就是：
        # return ''.join(chr(asc&95) if 96<=(asc:=ord(c))<=122 else c for c in s)
        res = ''
        for c in s:
            asc = ord(c)
            if 65<=ord(c)<=90:
                res += asc|32


s = Solution()
t = s.toLowerCase('asSAD_AS_-d')
print(t)