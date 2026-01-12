# Last updated: 1/12/2026, 1:41:26 PM
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = sum(dp[i-1][max(0, j-k):j]) % MOD
                
        return dp[n][target]