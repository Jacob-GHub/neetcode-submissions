class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        n = len(s)

        def decode(i):
            if i == n: 
                return 1
            if i < n and s[i] == "0": 
                return 0
            if i in dp:
                return dp[i]

            dp[i] = decode(i+1)
            if i + 1 < n and s[i:i+2] <= "26":
                dp[i] += decode(i+2)

            return dp[i]

        return decode(0)
