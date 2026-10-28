class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(1, amount + 1):
                if c <= i:
                    dp[i] = min(dp[i-c] + 1, dp[i])
                    
        if dp[amount] == INF:
            return -1
        else:
            return dp[amount]