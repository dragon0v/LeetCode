### 此题考点为多线程
# 确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

from typing import *
from threading import Lock

class Foo:
    def __init__(self):
        self.firstJobDone = Lock()  # 初始化一个锁
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()  # 获得一个锁，获得不了就一直等待
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()  # 释放1号锁

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:  # 1号锁没有释放时一直等待
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/print-in-order/solution/an-xu-da-yin-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。