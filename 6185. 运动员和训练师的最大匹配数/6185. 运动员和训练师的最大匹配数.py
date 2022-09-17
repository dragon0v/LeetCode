class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        last = trainers[-1]
        res = 0
        i = 0
        for p in players:
            # 这里一定要用i，不可以动trainers数组，不可以trainers = trainers[i+1:]
            while i<len(trainers):
                if trainers[i]>=p:
                    res += 1
                    i += 1
                    break
                # 最大的都满足不了，可以退出了
                if trainers[i]==last:
                    return res
                i += 1
            
        return res