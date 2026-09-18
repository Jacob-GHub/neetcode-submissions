class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # [1,2,3],
        # [4,5,6],
        # [7,8,9]

        # [3,2,1],
        # [6,5,4],
        # [9,8,7]

        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            matrix[r].reverse()
        
        for r in range(ROWS):
            for c in range(COLS - r - 1):
                matrix[r][c], matrix[COLS - c - 1][ROWS - r - 1] = matrix[COLS - c - 1][ROWS - r - 1], matrix[r][c]
        
