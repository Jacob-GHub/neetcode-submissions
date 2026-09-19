class Solution:
    def isHappy(self, n: int) -> bool:
        dp  = {}

        def happy(n):
            if n == 1:
                return True

            if n in dp:
                return False

            s = str(n)
            nxt = 0
            for num in s:
                nxt += int(num) ** 2
            
            dp[n] = nxt
            return happy(nxt)
        return happy(n)

