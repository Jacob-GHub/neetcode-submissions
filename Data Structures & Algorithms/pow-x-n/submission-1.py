class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}

        def makePow(n):
            if n in dp:
                return dp[n]
            
            if n == 1:
                return x
            
            if n % 2 != 0:
                dp[n] = x * makePow(n-1)
                return dp[n]
            
            half = n // 2
            dp[n] = makePow(half) * makePow(half)
            return dp[n]
        
        if n == 0: 
            return 1
        
        if n < 0:
            return 1 / makePow(abs(n))

        return makePow(n)
