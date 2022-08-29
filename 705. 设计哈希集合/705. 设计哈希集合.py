class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 997
        self.data=[[] for i in range(1000)]
        print(self.data)


    def add(self, key: int) -> None:
        idx = key % self.N
        # 判断是否已在哈希集合中，已在则不用添加
        if key not in self.data[idx]:
            self.data[idx].append(key)


    def remove(self, key: int) -> None:
        idx = key % self.N
        if key in self.data[idx]:
            self.data[idx].remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.N
        if key in self.data[idx]:
            return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

m = MyHashSet()
m.add(1)