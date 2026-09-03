class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def find_profit(i):
            if i >= n: 
                return 0
            
            if i in dp:
                return dp[i]

            dp[i] = find_profit(i + 1)

            # Buy on day i, sell on day j
            for j in range(i + 1, n):
                dp[i] = max(
                    dp[i],
                    prices[j] - prices[i] + find_profit(j + 2)
                )
            
            return dp[i]
        
        return find_profit(0)
