class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 其他情况判断
        if len(needle) > len(haystack):return -1
        if needle=="": return 0

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1,-1,-1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st)+1
            return dic
        
        # 偏移表预处理    
        dic = calShiftMat(needle)
        idx = 0
    
        while idx+len(needle) <= len(haystack):
            
            # 待匹配字符串
            str_cut = haystack[idx:idx+len(needle)]
            
            # 判断是否匹配
            if str_cut==needle:
                return idx
            else:
                # 边界处理
                if idx+len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]
            
        
        return -1 if idx+len(needle) >= len(haystack) else idx

# 作者：Tes
# 链接：https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 思路：
# 大致思路就是一个传统循环的比较算法的改进
# 传统方法每次比较temp:=haystack[i:i+len(needle)]是否等于needle，匹配返回i，不匹配i++，时间O(n*(n-m))
# 但是这个算法给出了一种优化方案，优化上面不匹配的情况
# 不是死板进行i++的操作，而是检查c:=temp[-1]是否在needle中，如果在，则i=i+shift[c] (shift为预处理的偏移表，重复字符位置为最后一次出现的下标)，如果不在则i=i+len(needle)
# 循环，直到 i+len(needle) > len(haystack)
# 时间最坏O(n*(n-m))，平均O(n)
