class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def rob2(nums):
            n = len(nums)

            if n <= 1: 
                return max(nums)

            previous, neighbor = nums[0], nums[1]
            
            for i in range(2, n):
                nums[i] += previous
                previous = max(neighbor, previous)
                neighbor = nums[i]
                
            return max(nums[n-1], nums[n-2])
        
        return max(rob2(nums[1:]), rob2(nums[:len(nums)-1]))

            