class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1

        for coin in coins:
            for i in range(amount+1):
                # if coin == i: 
                #     dp[i] += 1
                if coin <= i:
                    dp[i] += dp[i-coin]
        # print(dp)
        return dp[amount]
