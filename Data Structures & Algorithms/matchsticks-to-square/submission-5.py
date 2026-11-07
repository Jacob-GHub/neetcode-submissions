class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        matchsticks.sort(reverse = True)
        total = sum(matchsticks)
        target = total / 4

        if total % 2 != 0 or n < 4 or not target.is_integer(): 
            return False
        

        def backtrack(i,subsets):
            if i == n:
                return True
            stick = matchsticks[i]

            for j,num in enumerate(subsets):
                if stick + num <= target:
                    subsets[j] += stick
                    if backtrack(i+1, subsets):
                        return True
                    subsets[j] -= stick
            return False
        return backtrack(0,[0,0,0,0])
                
            
                    


                
         
        
        return backtrack(0,0,[0,0,0,0])
    
