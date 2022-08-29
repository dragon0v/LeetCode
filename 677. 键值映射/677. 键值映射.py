# from collections import 
class MapSum:

    def __init__(self):
        self.sortedkeys = []
        self.d = dict()

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
        self.sortedkeys.append(key)

    def sum(self, prefix: str) -> int:
        pk = []
        n = len(prefix)
        for key in self.d.keys():
            if len(key)>=n and key[:n]==prefix:
                pk.append(key)
        return sum(self.d[key] for key in pk)



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)