class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = {}

        def find_subsequence(i,j):
            if (i,j) in dp: 
                return dp[(i,j)]
            if i >= n or j >= m: 
                return 0

            if text1[i] == text2[j]: 
                dp[(i,j)] =  1 + find_subsequence(i+1,j+1)
            else:
                dp[(i,j)] = max(
                    find_subsequence(i+1,j),
                    find_subsequence(i,j+1)
                )

            return dp[(i,j)]
            
        find_subsequence(0,0)
        return dp[(0,0)]


