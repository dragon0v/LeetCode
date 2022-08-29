class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # 预处理桌号和菜名
        tables = []
        dishes = []
        for each in orders:
            tables.append(int(each[1]))
            dishes.append(each[2])
        tables = list(set(tables))
        tables.sort()
        dishes = list(set(dishes))
        dishes.sort()

        dt = {}
        for i,v in enumerate(tables):
            dt[v]=i
        print(dt)
        dd = {}
        for i,v in enumerate(dishes):
            dd[v]=i

        res = [[0 for _ in range(len(dishes)+1)] for _ in range(len(tables)+1)]
        res[0] = ['Table']+dishes
        for i in range(len(tables)):
            res[i+1][0] = tables[i]
        #print(res)
        for each in orders:
            res[dt[int(each[1])]+1][dd[each[2]]+1] += 1
        
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = str(res[i][j])
        return res