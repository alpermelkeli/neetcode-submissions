class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(0, amount + 1):
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        if dp[-1] == INF: 
            return -1
        return dp[-1]
