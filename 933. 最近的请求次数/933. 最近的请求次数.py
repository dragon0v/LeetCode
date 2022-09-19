class RecentCounter:
    def __init__(self):
        self.queue = []  # 队列储存当前的请求时间，有新的请求进入时先删去过时的请求，再加入

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0]+3000 < t:
            del self.queue[0]
        self.queue.append(t)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# 308 ms	19.7 MB