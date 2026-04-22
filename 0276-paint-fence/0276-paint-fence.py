class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[k, 0]]
        for i in range(n):
            dp.append([dp[i][0]*(k-1)+dp[i][1]*(k-1), dp[i][0]])
        return dp[n-1][0] + dp[n-1][1]