class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        n, m = len(s), len(p)

        def findMatch(i, j):
            if j == m:
                return i == n

            if (i, j) in dp:
                return dp[(i, j)]

            firstMatch = i < n and (p[j] == s[i] or p[j] == ".")

            if j + 1 < m and p[j + 1] == "*":
                # Option 1: use zero occurrences of p[j]
                # Option 2: consume one character and stay on p[j]*
                dp[(i, j)] = (
                    findMatch(i, j + 2)
                    or (firstMatch and findMatch(i + 1, j))
                )
            else:
                dp[(i, j)] = (
                    firstMatch
                    and findMatch(i + 1, j + 1)
                )

            return dp[(i, j)]

        return findMatch(0, 0)