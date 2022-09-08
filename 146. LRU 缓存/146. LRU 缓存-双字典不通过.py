from collections import Counter, defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = defaultdict(lambda:-1)  # key:value
        self.freq = Counter()  # key:freq
        self.maxcap = capacity
        self.cur = 0  # 当前容量
        self.t = 2*100000+99  # 最后使用的时间，每次进行操作-1，配合most_common实现最近最少使用

    def get(self, key: int) -> int:
        # 不存在直接返回
        if self.dic[key]==-1:
            return -1
        # 存在，更新freq，返回结果
        self.t -= 1
        self.freq[key] = self.t

        return self.dic[key]


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # 执行替换操作，直接替换，更新
            self.dic[key] = value
            self.t -= 1
            self.freq[key] = self.t
        else:
            # 执行插入操作，然后判断缓存是否已满
            self.cur += 1
            self.dic[key] = value
            self.t -= 1
            self.freq[key] = self.t

            if self.cur > self.maxcap:
                # 缓存已满,需要抛弃freq值最大的那个
                # print('del',self.freq.most_common(1)[0][0])
                delk = self.freq.most_common(1)[0][0]
                del self.dic[delk]
                del self.freq[delk]
                self.cur -= 1

### 过不了，应该输出-1的输出了值，说明抛弃的部分写错了?

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)