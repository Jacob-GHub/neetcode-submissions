class Solution:
    def countSubstrings(self, s: str) -> int:
        pali_count = 0
        n = len(s)

        def expand(l,r):
            nonlocal pali_count
            if l < 0 or r >= n:
                return

            while l >= 0 and r < n and s[l] == s[r]:
                pali_count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        
        return pali_count