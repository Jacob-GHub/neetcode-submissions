class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pali = 1
        index_pali = 0

        def expand(l, r):
            nonlocal longest_pali, index_pali

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest_pali:
                    longest_pali = r - l + 1
                    index_pali = l

                l -= 1
                r += 1

        for i in range(len(s)):
            # Odd-length palindrome
            expand(i, i)

            # Even-length palindrome
            expand(i, i + 1)

        return s[index_pali:index_pali + longest_pali]