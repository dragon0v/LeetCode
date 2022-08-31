class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 模拟，每次向前找符合条件的k张牌
        # 时间超过5%，空间超过99%
        # 能AC是因为这题条件比较宽松，一样的1296就过不了
        if len(hand)%groupSize:
            print(11)
            return False
        
        hand.sort()
        print(hand)
        while len(hand)>0:
            m = hand.pop(0)
            print(m)
            for k in range(groupSize-1):
                i = 0
                while i<len(hand):
                    if hand[i]==m+1:
                        m = hand.pop(i)
                        print(m)
                        break
                    if hand[i]>m+1:
                        return False
                    i += 1
                if i==len(hand) and hand!=[]:
                    return False

        return True
