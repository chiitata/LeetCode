from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        count = 0
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    que = deque([(i, j)])
                    while que:
                        x, y = que.popleft()
                        for xx, yy in direct:
                            if 0<= xx+x <n and 0<= yy + y <m and grid[xx+x][yy+y] == "1":
                                que.append((xx+x, yy+y))
                                grid[xx+x][yy+y] = 0
        return count

                    