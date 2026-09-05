class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = collections.defaultdict(bool)
        if len(s1) + len(s2) > len(s3):
            return False

        def can_interleave(i,j):
            cur = i + j
            if cur >= len(s3):
                return True 

            if (i,j) in dp:
                return dp[(i,j)]
                
            if i < len(s1) and s1[i] == s3[cur]:
                dp[(i,j)] = dp[(i,j)] or can_interleave(i+1,j)
            
            if j < len(s2) and s2[j] == s3[cur]:
                dp[(i,j)] = dp[(i,j)] or can_interleave(i,j+1)

            return dp[(i,j)]

        return can_interleave(0,0)

