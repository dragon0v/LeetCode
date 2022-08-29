class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and ':' in queryIP:
            return 'Neither'
        if '.' in queryIP:
            l = queryIP.split('.')
            if len(l)!=4:
                return 'Neither'
            for n in l:
                if len(n)>1 and n[0]=='0':
                    return 'Neither'
                if not n.isdigit():
                    return 'Neither'
                if 0>int(n) or int(n)>255:
                    return 'Neither'
            return 'IPv4'
        else:
            l = queryIP.split(':')
            if len(l)!=8:
                return 'Neither'
            for n in l:
                if len(n)>4 or len(n)<1:
                    return 'Neither'
                for c in n:
                    if c not in '1234567890abcdefABCDEF':
                        return 'Neither'
            return 'IPv6'

# 没啥意思，有点面向用例编程的感觉了，不过一次过也是有难度的