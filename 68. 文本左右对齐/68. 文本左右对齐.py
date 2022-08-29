class Solution:
    def fullJustify(self, words, maxWidth: int):
        def place(li):
            if len(li)==1:
                return li[0] + ' ' * (maxWidth-len(li[0]))
            # 计算空格总数和间隔数量
            spaces = maxWidth - sum(len(each) for each in li)
            for i in range(spaces):
                li[i % (len(li)-1)] += ' '
            
            return ''.join(li)

        res = []
        crt_len = len(words[0])
        crt_words = [words[0]]
        # 第一步找到能放在一行的若干words
        # 第二步按规则放进去
        for each in words[1:]:
            if crt_len + 1 + len(each) <= maxWidth:
                crt_len += 1 + len(each)
                crt_words.append(each)
            else:
                res.append(place(crt_words))
                crt_len = len(each)
                crt_words = [each]

        # 最后一组特殊处理
        t = ' '.join(crt_words)
        res.append(t + ' ' * (maxWidth-len(t)))

        return res

s = Solution()
t = s.fullJustify(["Listn"],6)
print(t)