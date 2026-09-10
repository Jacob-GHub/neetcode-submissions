class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}

        def jump(i):
            if i >= n-1:
                return True
            
            if nums[i] == 0:
                return False
            
            if i in dp:
                return dp[i]
            
            dp[i] = False
            for j in range(i+1,1 + i + nums[i]):
                dp[i] = dp[i] or jump(j)
            
            return dp[i]
        
        return jump(0)
                
