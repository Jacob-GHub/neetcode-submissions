class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(row,col):
            if (
                (row,col) not in visited and 
                0 <= row < ROWS and 
                0 <= col < COLS and 
                board[row][col] == "O"
            ):
                visited.add((row,col))
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)

        for row in range(ROWS):
            if board[row][0] == "O": dfs(row,0)
            if board[row][COLS-1] == "O": dfs(row,COLS-1)
        
        for col in range(COLS):
            if board[0][col] == "O": dfs(0,col)
            if board[ROWS-1][col] == "O": dfs(ROWS-1,col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row,col) not in visited:
                    board[row][col] = "X"