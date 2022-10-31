class Solution:
    def magicalString(self, n: int) -> int:
        # 按题意模拟，时间空间后10%
        s = "1221121221221121122"
        while len(s)<n:
            news = []  # 每次新生成一段更长的s
            c = '12'  # 1,2 交替出现，先1后2
            i = 0  # 控制交替
            for repeat in s:
                news.append(int(repeat)*c[i%2])
                i += 1
            s = ''.join(news)
        # print(s)
        return Counter(s[:n])['1']