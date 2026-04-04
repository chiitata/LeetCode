from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == False:
                    que = deque()
                    que.append((i, j))
                    while que:
                        a, b = que.popleft()
                        if visited[a][b]:
                            continue
                        visited[a][b] = True
                        ans = self.is_island(grid, a, b, m, n)
                        for t in ans:
                            que.append(t)
                    else:
                        count += 1
        return count
    def is_island(self, grid, a, b, m, n):
        ans = []
        if a+1 <= m-1:
            if grid[a+1][b] == "1":
                ans.append((a+1, b))
        if a-1 >= 0:
            if grid[a-1][b] == "1":
                ans.append((a-1, b))
        if b+1 <= n-1:
            if grid[a][b+1] == "1":
                ans.append((a, b+1))
        if b-1 >= 0:
            if grid[a][b-1] == "1":
                ans.append((a, b-1))
        return ans