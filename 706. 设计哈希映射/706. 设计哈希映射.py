class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = [[] for _ in range(20011)] #创建一个大质数的数组,每个元素存放键值对数组

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        t = key % 20011
        for each in self.bucket[t]:
            if each[0] == key:
                each[1] = value
                return
        self.bucket[t].append([key,value])
        
            

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        t = key % 20011
        for each in self.bucket[t]:
            if(each[0]==key):
                return each[1]
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        t = key % 20011
        for each in self.bucket[t]:
            if(each[0]==key):
                self.bucket[t].remove(each)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)