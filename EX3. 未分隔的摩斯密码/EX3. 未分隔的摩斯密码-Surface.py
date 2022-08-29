MorseList = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    # ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    # "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    # "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
    # "....": "&", ".--.-.": "@", ".-.-.": "+",
}
# 原文链接：https://blog.csdn.net/weixin_42109012/article/details/97639972

class Solution:
    def findall(self,morse):
        self.res = []
        def dfs(idx,p,stack,lastidx=0):
            print(idx,p,stack,self.res,lastidx)
            if idx<lastidx:
                stack.pop(-1)
            lastidx = idx+p
            if idx == 0:
                stack = [] # 存放当前获得的字符
            elif idx+p > len(morse):
                return
                
            print(morse[idx:idx+p])
            if morse[idx:idx+p] in MorseList.keys():
                stack.append(MorseList[morse[idx:idx+p]])
                added = True
                # 到达结尾
                if idx+p == len(morse):
                    self.res.append(''.join(stack))
                    return
                
                else:
                    dfs(idx+p,1,stack,lastidx)
                    dfs(idx+p,2,stack,lastidx)
                    dfs(idx+p,3,stack,lastidx)
                    dfs(idx+p,4,stack,lastidx)
                    dfs(idx+p,5,stack,lastidx)
                    
            # 当前词不在词典中
            else:
                return
        
        dfs(0,1,[])       
        dfs(0,2,[])       
        dfs(0,3,[])       
        dfs(0,4,[])       
        dfs(0,5,[])       
        
        return self.res

s = Solution().findall('.-.')
print(s)

# '.-.': ['ETE', 'EN', 'AE', 'R']
# '.-..---...-.' 包含love