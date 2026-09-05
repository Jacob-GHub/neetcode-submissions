class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        largest_path = 1

        def findPath(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            cur_value = matrix[i][j]
            longest_path = 1
            for x,y in directions:
                ni,nj = i + x, j + y
                if (0 <= ni < ROWS and 0 <= nj < COLS) and cur_value < matrix[ni][nj]:
                    longest_path = max(longest_path, 1 + findPath(ni,nj))
            
            dp[(i,j)] = longest_path
            return longest_path

    
        for row in range(ROWS):
            for col in range(COLS):
                largest_path = max(largest_path, findPath(row,col))
        return largest_path