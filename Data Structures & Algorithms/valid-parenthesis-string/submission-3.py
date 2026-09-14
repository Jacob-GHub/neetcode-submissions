class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts, stars = [], []
        
        for i in range(len(s)):
            if s[i] == "(":
                lefts.append(i)
            elif s[i] == "*":
                stars.append(i)
            else:
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while lefts:
            if not stars:
                return False
            elif stars.pop() < lefts.pop():
                return False
        
        return True
