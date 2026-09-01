class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = collections.defaultdict(bool)
        dp[0] = True

        if sum(nums) % 2:
            return False
            
        target = sum(nums)//2

        for i, num in enumerate(nums):
            for j in range(target,num-1,-1):
                dp[j] = dp[j] or dp[j-num]

        return dp[target]

