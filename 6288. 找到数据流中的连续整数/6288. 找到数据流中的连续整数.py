class DataStream:
    def __init__(self, value: int, k: int):
        self.tar = value
        self.k = k
        self.cur = 0

    def consec(self, num: int) -> bool:
        if num==self.tar:
            self.cur += 1
            if self.cur>=self.k:
                return True
        else:
            self.cur = 0
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)