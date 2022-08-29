class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # typed 只会大于等于原名字
        if len(typed)<len(name):
            return False
        if name[0]!=typed[0]:
            return False
        
        # 双指针
        i,j = 1,1
        # while i<len(name) and j < len(typed):
        while 1:
            if name[i] == typed[j]:
                i,j = i+1,j+1
            else:
                if typed[j]==typed[i]:
                    # typed出现长按
                    j+=1
                else:
                    # typed和name不对应
                    return False
            
            if i == len(name)-1:
                # name 遍历到底了，如果剩下的typed不是相同的字符就说明不对应
                for k in range(j+1,len(typed)):
                    if typed[k] != typed[j+1]:
                        return False
                return True

                



# "aalex"
# "alex"

# "alex"
# "aalexb"

# "a"
# "b"
s = Solution()
print(s.isLongPressedName("a","aa"))