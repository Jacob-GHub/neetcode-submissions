class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        n,m = len(word1), len(word2)

        def edit(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < n and j >= m:
                return n-i
            
            if i >= n and j < m: 
                return m-j
            
            if i >= n and j >= m: 
                return 0

            if word1[i] == word2[j]:
                dp[(i,j)] = edit(i+1,j+1)
            else:
                dp[(i,j)] = min(edit(i+1,j), edit(i,j+1), edit(i+1,j+1)) + 1
            
            return dp[(i,j)]
        
        return edit(0,0)

            

            
