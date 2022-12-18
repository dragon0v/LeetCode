class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # 周赛摆烂做法
        hash = []
        for w in words:
            hash.append(str(sorted(Counter(w).keys())))  # 这里不应该用Counter(w).keys()，list(set(w))会更好
        print(hash)
        c = Counter(hash)
        res = 0
        for x in c.values():
            res += x*(x-1)
        return res//2