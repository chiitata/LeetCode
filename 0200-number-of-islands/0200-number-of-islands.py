from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)]for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and grid[i][j] == "1":
                    que = deque()
                    que.append((i, j))
                    visited[i][j] = True
                    while que:
                        x, y = que.pop()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if 0<=x+dx<n and 0<=y+dy<m:
                                if visited[x+dx][y+dy] == False and grid[x+dx][y+dy] == "1":
                                    que.append((x+dx, y+dy))
                                    visited[x+dx][y+dy] = True
                    else:
                        ans += 1
        return ans     