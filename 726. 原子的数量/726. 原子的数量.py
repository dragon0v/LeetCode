from collections import defaultdict


class Solution:
    def countOfAtoms(self, s: str) -> str:
        # 如何确定每个原子
        # 如何进行数量统计
        # 如何按字典序返回答案

        # 从后往前遍历+将数字入栈
        st = [1]
        i = len(s)-1
        d = defaultdict(int)
        lower = ''  # 
        count = ''  #
        while i>-1:
            if '0' <= s[i] <= '9':
                count = s[i] + count
            elif 'a' <= s[i] <= 'z':
                lower = s[i] + lower
            elif s[i] == ')':
                st.append(st[-1] * int(count or '1'))  # int(count or '1')很巧妙，count为空则int('x')=x
                count = ''
            elif s[i] == '(':
                st.pop()
            elif 'A' <= s[i] <= 'Z':
                d[s[i] + lower] += st[-1] * int(count or '1')
                count = ''
                lower = ''
            i -= 1

        ans = ''
        for k, v in sorted(d.items()):  # 在这里用sorted进行字典序返回
            if v == 1:
                ans += k
            else:
                ans += k + str(v)
        return ans

# 作者：fe-lucifer
# 链接：https://leetcode.cn/problems/number-of-atoms/solution/li-kou-jia-jia-cong-hou-wang-qian-bian-l-h6bz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。