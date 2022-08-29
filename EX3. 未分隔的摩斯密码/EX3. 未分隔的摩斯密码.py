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
        self.lastidx = 0
        def dfs(idx,p,stack):
            # print(idx,p,stack,self.res,self.lastidx)
            if idx<self.lastidx and idx!=0:
                stack.pop(-1)
            self.lastidx = idx
            
            if idx+p > len(morse):
                return
                
            # print(morse[idx:idx+p])
            if morse[idx:idx+p] in MorseList.keys():
                stack.append(MorseList[morse[idx:idx+p]])
                added = True
                # 到达结尾
                if idx+p == len(morse):
                    self.res.append(''.join(stack))
                    stack.pop(-1)
                    return
                
                else:
                    dfs(idx+p,1,stack)
                    dfs(idx+p,2,stack)
                    dfs(idx+p,3,stack)
                    dfs(idx+p,4,stack)
                    dfs(idx+p,5,stack)
                    
            # 当前词不在词典中
            else:
                return
        
        dfs(0,1,[])       
        dfs(0,2,[])       
        dfs(0,3,[])       
        dfs(0,4,[])       
        dfs(0,5,[])       
        
        return self.res

s = Solution().findall('.-..---...-.')
print(len(s))
for e in s:
    print(e)
print('LOVE' in s)
# '.-.': ['ETE', 'EN', 'AE', 'R']
# '.-..---...-.' 包含love

# 结果还是不对