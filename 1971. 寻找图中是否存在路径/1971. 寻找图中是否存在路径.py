class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 800ms 11%，276MB 189%
        # 优化思路是递归转循环 或 并查集
        if n==1:
            return True
        conn = [[] for _ in range(n)]
        for a,b in edges:
            conn[a].append(b)
            conn[b].append(a)
        print(conn)

        visited = [False for _ in range(n)]
        print(visited)
        self.flag = False  # 总感觉不够优雅
        def dfs(source):
            # print(source, conn[source])
            if visited[source]:
                return
            visited[source] = True
            for c in conn[source]:
                if c==destination:
                    self.flag = True
                    return True
                dfs(c)
            return
        
        dfs(source)

        return self.flag
