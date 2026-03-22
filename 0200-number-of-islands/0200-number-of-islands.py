from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        checked = [[False for _ in range(n)]for _ in range(m)]
        q = deque()
        ans = 0

        def check(tuple):
            x, y = tuple
            checked[x][y] == True
            q.append((x, y))
            while q:
                x, y = q.pop()
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xi = x+i
                    yi = y+j
                    if xi < m and xi >= 0 and yi < n and yi >= 0:
                        if grid[xi][yi] == "1" and not checked[xi][yi]:
                            q.append((xi, yi))
                            checked[xi][yi] = True
            return 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not checked[i][j]:
                    ans += check((i, j))
        return ans
        