from collections import deque


class RecentCounter:
    def __init__(self):
        # 此版本使用了deque代替list
        self.queue = deque()  # 队列储存当前的请求时间，有新的请求进入时先删去过时的请求，再加入

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0]+3000 < t:
            self.queue.popleft()  # deque的这个操作时时间快了80ms
        self.queue.append(t)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# 224 ms	19.7 MB