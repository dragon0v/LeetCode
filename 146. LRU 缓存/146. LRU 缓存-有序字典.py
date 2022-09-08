from collections import Counter, defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.maxcap = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            t = self.dic[key]
            del self.dic[key]
            self.dic[key] = t
            return t
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 替换
        if key in self.dic:
            del self.dic[key]
            self.dic[key] = value
            return 
        # 添加
        self.dic[key] = value
        # 删除
        if len(self.dic) > self.maxcap:
            for one in self.dic:
                del self.dic[one]
                return  # 循环+return 这里很巧妙
        

### py36之后默认的dict就是有序的，此解法时间击败90%，空间99%

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)