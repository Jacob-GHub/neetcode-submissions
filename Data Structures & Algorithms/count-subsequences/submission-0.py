class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        dp = {}

        def findDistinct(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if j == m:
                return 1

            if i >= n:
                return 0

            if s[i] == t[j]:
                dp[(i,j)] = findDistinct(i+1,j+1)

            dp[(i,j)] = dp.get((i,j), 0) + findDistinct(i+1,j)
            return dp[(i,j)]

        findDistinct(0,0)
        print(dp)
        return dp[(0,0)]
