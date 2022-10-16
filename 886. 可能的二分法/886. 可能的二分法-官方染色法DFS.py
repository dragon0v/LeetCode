class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # https://leetcode.cn/problems/possible-bipartition/solutions/1893341/ke-neng-de-er-fen-fa-by-leetcode-solutio-guo7/
        # 官解 染色法+DFS
        # 无论是从题目描述和对点边的描述，这都是一道「染色法判定二分图」的模板题。
        # TODO 理解dfs的条件
        # TODO BFS和并查集解法
        
        g = [[] for _ in range(n)]  # 储存dislike信息，例如g[a] = [b,c,d]说明a不可以和bcd分到一组
        for x, y in dislikes:
            # 使dislikes中的每组xy 在g中可以互相查到
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x
        def dfs(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])

        return all(c or dfs(i, 1) for i, c in enumerate(color))  # dfs里的c除了这里的1和-1也可以用1和2，对应dfs(y,3-c)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/possible-bipartition/solutions/1893341/ke-neng-de-er-fen-fa-by-leetcode-solutio-guo7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。