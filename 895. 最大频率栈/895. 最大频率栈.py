from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.freq = Counter()  # 记录值对应的频率
        self.group = defaultdict(list)  # 记录频率对应的所有值，栈顶的元素会在值列表的最后

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)  # 不需要删除group[freq[val]-1]中的val，很巧妙


    def pop(self) -> int:
        print(self.freq.most_common(1))
        freq = self.freq.most_common(1)[0][1]
        val = self.group[freq].pop()
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# 看了官解写的
# 超时，是因为mostcommon耗时久吗 - 增加most_freq就可以了