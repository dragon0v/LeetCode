class Solution:
    def partitionLabels(self, S: str):
        # 中等，贪心

        res = []

        # 首先预处理，得到a-z的最先和最后出现的位置
        az = [[-1,-1] for _ in range(26)]
        for i in range(len(S)):
            # 首次出现位置
            if az[ord(S[i])-ord('a')][0] == -1:
                az[ord(S[i])-ord('a')][0] = i
            # 最后出现位置
            az[ord(S[i])-ord('a')][1] = i

        az.sort(key=lambda li:li[0])
        print(az)

        # [[-1,-1],...,|[0, 8], [1, 5], [4, 7], [9, 14], [10, 15], [11, 11], [13, 13], [16, 19], [17, 22], [18, 23], [20, 20], [21, 21]]
        
        res = []
        seg = [0,-1]
        for each in az:
            # -1表示没出现这个字母，直接跳过
            if each[0] != -1:
                # 当前范围下界在seg内且上界在seg后，应该拓展seg
                if each[0] < seg[1] and each[1] > seg[1]:
                    seg[1] = each[1]
                # 当前范围下界在seg后，说明可以进行分割，然后以当前范围为新的seg
                if each[0] > seg[1]:
                    res.append(seg[1]-seg[0]+1)
                    print(seg)
                    seg = each
        # 最后一次处理
        res.append(seg[1]-seg[0]+1)
        return res[1:]

        # 过了，但是上面的res[1:]肯定可以优化

s = Solution()
t = s.partitionLabels("ababcbacadefegdehijhklij")
print(t)