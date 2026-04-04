from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        
        # 4方向の移動を定義（エンジニアっぽく！）
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                # 陸地かつ未訪問なら新しい島を発見
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    que = deque([(i, j)])
                    visited[i][j] = True  # 追加する時に訪問済みにする
                    
                    while que:
                        curr_i, curr_j = que.popleft()
                        
                        # その場の4近傍をチェック
                        for di, dj in directions:
                            ni, nj = curr_i + di, curr_j + dj
                            
                            # 範囲内 かつ 陸地 かつ 未訪問
                            if 0 <= ni < m and 0 <= nj < n and \
                               grid[ni][nj] == "1" and not visited[ni][nj]:
                                visited[ni][nj] = True
                                que.append((ni, nj))
                                
        return count