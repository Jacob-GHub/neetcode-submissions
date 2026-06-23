class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        

        def backtracking(i,currSum):
            if currSum == target:
                res.append(subset.copy())
                return
            if currSum > target or i >=len(candidates):
                return
            
            subset.append(candidates[i])
            currSum += candidates[i]
            backtracking(i+1,currSum)

            currSum -= subset.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+=1
            backtracking(i+1,currSum)
        
        backtracking(0,0)
        return res