class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 整活向 脑溢血代码
        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        premon = [0]
        for i in range(12):
            premon.append(premon[-1]+mon[i])
        print(premon)
        aaa = [0 for i in range(366)]
        bbb = [0 for _ in range(366)]
        a1,a2 = arriveAlice.split('-')
        a3,a4 = leaveAlice.split('-')
        b1,b2 = arriveBob.split('-')
        b3,b4 = leaveBob.split('-')
        astart = 1*premon[int(a1)-1] + int(a2)
        aend = premon[int(a3)-1] + int(a4)
        bstart = 1*premon[int(b1)-1] + int(b2)
        bend = premon[int(b3)-1] + int(b4)
        
        for i in range(astart,aend+1):
            aaa[i] = 1
        for i in range(bstart,bend+1):
            bbb[i] = 1
        
        return sum([(x==1 and 1==y) for x,y in zip(aaa,bbb)])