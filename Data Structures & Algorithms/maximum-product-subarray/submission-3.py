class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            max_sum = 1
            min_sum = 1
            max_product = float('-inf')

            for num in nums:
                run_sum = max_sum * num
                max_sum = max(num, run_sum, min_sum * num)
                min_sum = min(run_sum, min_sum * num, num)
                max_product = max(max_sum,max_product)
            
            return max_product
            


