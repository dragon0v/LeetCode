from collections import Counter, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.maxcap = capacity
        self.freq = Counter()
        self.d = dict()
        self.f = 10000009

    def get(self, key: int) -> int:
        if key in self.d:
            del self.freq[key]
            self.f -= 1
            self.freq[key] = self.f
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # 无论如何都要更新freq
        del self.freq[key]
        self.f -= 1
        self.freq[key] = self.f

        if key in self.d:
            self.d[key] = value
            return 

        if len(self.d)==self.maxcap:
            delk = self.freq.most_common(1)[0][0]
            print(delk)
            self.f -= 1
            del self.freq[delk]
            del self.d[delk]
        
        self.d[key] = value
        
# 有问题，AC不了


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)