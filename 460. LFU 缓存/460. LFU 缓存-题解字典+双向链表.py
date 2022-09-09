class DLNode:
    def __init__(self, key, val, cnt=0):
        self.val = [key, val, cnt]  # 键、值、访问次数
        self.pre = None
        self.nxt = None


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # 通过key保存链表节点，key:node
        self.c = capacity  # 字典容量
        self.head = DLNode(1, 1, float('inf'))  # 头节点，定义访问次数正无穷
        self.tail = DLNode(-1, -1, float('-inf'))  # 尾节点，定义访问次数负无穷
        self.head.nxt = self.tail 
        self.tail.pre = self.head

    def _refresh(self, node, cnt):  #   # 辅助函数，对节点node，以访问次数cnt重新定义其位置
        pNode, nNode = node.pre, node.nxt   # 当前节点的前后节点
        if cnt < pNode.val[2]:  # 如果访问次数小于前节点的访问次数，无需更新位置
            return
        pNode.nxt, nNode.pre = nNode, pNode  # 将前后连起来，跳过node位置
        while cnt >= pNode.val[2]:  # 前移到尽可能靠前的位置后插入
            pNode = pNode.pre
        nNode = pNode.nxt
        pNode.nxt = nNode.pre = node
        node.pre, node.nxt = pNode, nNode

    def get(self, key: int) -> int:
        if self.c <= 0 or key not in self.cache:  # 如果容量<=0或者key不在字典中，直接返回-1
            return -1
        node = self.cache[key]  # 通过字典找到节点
        _, value, cnt = node.val  # 通过节点得到key，value和cnt
        node.val[2] = cnt+1  # 访问次数+1
        self._refresh(node, cnt+1)  # 刷新位置
        return value

    def put(self, key: int, value: int) -> None:
        if self.c <= 0:  # 缓存容量<=0
            return
        if key in self.cache:  # 已在字典中，则要更新其value，同时访问次数+1刷新位置
            node = self.cache[key]
            _, _, cnt = node.val
            node.val = [key, value, cnt+1]  # 更新其值
            self._refresh(node, cnt+1)
        else:
            if len(self.cache) >= self.c:   # 容量已满，先清除掉尾部元素
                tp, tpp = self.tail.pre, self.tail.pre.pre
                self.cache.pop(tp.val[0])   # 从字典剔除尾节点
                tpp.nxt, self.tail.pre = self.tail, tpp   # 首尾相连，跳过原尾节点
            node = DLNode(key, value)  # 新建节点，并插入到队尾，再刷新其位置
            node.pre, node.nxt = self.tail.pre, self.tail
            self.tail.pre.nxt, self.tail.pre = node, node
            self.cache[key] = node
            self._refresh(node, 0)

# 超时

# 作者：luanhz
# 链接：https://leetcode.cn/problems/lfu-cache/solution/pythonshuang-xiang-lian-biao-zi-dian-jian-dan-yi-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。