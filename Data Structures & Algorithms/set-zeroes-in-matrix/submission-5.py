class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix), len(matrix[0])
        first_row = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0

            
        if first_row:
            for j in range(m):
                matrix[0][j] = 0
                    


        