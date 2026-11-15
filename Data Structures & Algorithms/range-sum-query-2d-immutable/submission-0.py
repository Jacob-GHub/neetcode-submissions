class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n,m = len(self.matrix), len(self.matrix[0])

        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    self.matrix[i][j] -= self.matrix[i-1][j-1]
                if i > 0:
                    self.matrix[i][j] += self.matrix[i-1][j]
                if j > 0:
                    self.matrix[i][j] += self.matrix[i][j-1]
        print (self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region = self.matrix[row2][col2]

        if row1 > 0 and col1 > 0:
            region += self.matrix[row1-1][col1-1]
        
        if row1 > 0:
            region -= self.matrix[row1-1][col2]
        
        if col1 > 0:
            region -= self.matrix[row2][col1-1]
        
        return region



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)