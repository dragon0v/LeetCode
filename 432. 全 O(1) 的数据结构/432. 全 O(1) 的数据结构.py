class AllOne:

    def __init__(self):
        self.strs = [set() for _ in range(50005)]
        self.dic = {} # 记录存在的key和数量
        self.cnt = 0 # =len(self.dic.keys())x
        self.maxidx = -1
        self.minidx = 100000


    def inc(self, key: str) -> None:
        if key in self.dic.keys():
            idx = self.dic[key]
            self.strs[idx].remove(key) # o(1)
            self.strs[idx+1].add(key)
            if idx==self.minidx and len(self.strs[idx])==0:
                self.minidx += 1
            self.dic[key] += 1
            self.maxidx = max(self.maxidx,idx+1)
        else:
            self.strs[1].add(key)
            self.cnt += 1 # 表示新增加了key
            self.dic[key] = 1
            self.maxidx = max(self.maxidx,1)
            self.minidx = min(self.minidx,1)

    def dec(self, key: str) -> None:
        idx = self.dic[key]
        self.strs[idx].remove(key)
        self.strs[idx-1].add(key)
        if idx==self.maxidx and len(self.strs[idx])==0:
            self.maxidx -= 1
        if idx==self.minidx and len(self.strs[idx])==0: 
            self.minidx -= 1
            if self.minidx==0 and self.cnt>0: #当minidx从1->0时需要重新计算minidx
                
        self.dic[key] -= 1
        if idx==1:
            self.cnt -= 1 # 表示减少了key，此时在self.dic[0]中仍有key

    def getMaxKey(self) -> str:
        if self.cnt==0:
            return ''
        t = self.strs[self.maxidx] #o(1)
        tt = t.pop()
        t.add(tt)
        return tt
        
    def getMinKey(self) -> str:
        if self.cnt==0:
            return ''
        t = self.strs[self.minidx]
        tt = t.pop()
        t.add(tt)
        return tt



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()