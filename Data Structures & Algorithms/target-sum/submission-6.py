class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def find_sum(i,target):
            if i == len(nums):
                return target == 0
            
            if (i,target) in dp:
                return dp[(i,target)]
            
            dp[(i,target)] = find_sum(i+1,target - nums[i]) + find_sum(i+1,target + nums[i])
            return dp[(i,target)]
        
        return find_sum(0,target)