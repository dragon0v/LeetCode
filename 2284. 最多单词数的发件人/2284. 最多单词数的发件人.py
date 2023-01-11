class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # 应该是自定义数据结构的知识点，简单题
        d = defaultdict(int)
        crtmax = 0
        crtname = ''
        for m,n in zip(messages,senders):
            d[n] += len(m.split(' '))
            if d[n] > crtmax:
                crtname = n
                crtmax = d[n]
            elif d[n] == crtmax:
                crtname = max(crtname,n)
        return crtname