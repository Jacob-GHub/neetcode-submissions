class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}
        n = len(s)

        def canBreak(i):
            if i in dp: 
                return dp[i]
            if i >= n:
                return True
            for j in range(i,n):
                if s[i:j+1] in wordDict and canBreak(j+1):
                    dp[i] = True
                    return True
            
            dp[i] = False
            return dp[i]
        
        canBreak(0)
        return dp[0]
