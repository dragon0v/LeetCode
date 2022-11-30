from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.freq = Counter()  # 记录值对应的频率
        self.group = defaultdict(list)  # 记录频率对应的所有值，栈顶的元素会在值列表的最后
        self.most_freq = 0

    def push(self, val: int) -> None:
        t = self.freq[val] + 1
        self.freq[val] = t
        self.group[t].append(val)  # 不需要删除group[freq[val]-1]中的val，很巧妙
        self.most_freq = max(self.most_freq,t)


    def pop(self) -> int:
        val = self.group[self.most_freq].pop()
        self.freq[val] -= 1
        if self.group[self.most_freq]==[]:
            self.most_freq -= 1  # 只需要-1，因为group没有删除操作，而group必定是+1上来的，很巧妙

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# 看了官解做的，
# 凭感觉的话counter的most_common操作应该是很快的，但事实似乎并不是这样
# 可以看看counter的文档