class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        num_islands = 0

        def dfs(row,col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row,col) in visited:
                return

            visited.add((row,col))
            for x,y in dirs:
                new_row, new_col = row+x, col+y
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == "1":
                    dfs(new_row,new_col)
            return

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in visited:
                    # print(row,col)
                    dfs(row,col)
                    # print(visited)
                    num_islands += 1
        return num_islands