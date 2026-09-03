class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def find_sum(i,target):
            if i == len(nums) - 1:
                if target == nums[i] or target == -nums[i]:
                    if nums[i] == 0: 
                        return 2
                    return 1
                
            if i >= len(nums): 
                return 0
            
            if (i,target) in dp:
                return dp[(i,target)]
            
            dp[(i,target)] = find_sum(i+1,target - nums[i]) + find_sum(i+1,target + nums[i])
            return dp[(i,target)]
        
        return find_sum(0,target)