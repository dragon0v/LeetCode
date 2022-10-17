class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 思路：遍历
        ans = 1
        n = len(fruits)
        trees = set()  # 当前果树的种类
        change=last=-1  # change是最后一次果树种类改变的位置，last是上一个果树的种类
        i = 0
        while i<n:
            for j in range(i,n):
                if fruits[j] not in trees:
                    # 出现新的树种，1：已有两种树，进行“结算”；2：未满，添加进树种
                    if len(trees)==2:
                        ans = max(ans,j-i)
                        i = change
                        trees = set()
                        break
                    else:
                        trees.add(fruits[j])
                if fruits[j]!=last:
                    change = j
                last = fruits[j]
            if j==n-1:
                break
        
        print(i,j,last,change)
        return max(ans,j-i+1)  # 最后一次j=n-1所以需要+1，之前的逻辑j是往前一个的，所以+1-1抵消了