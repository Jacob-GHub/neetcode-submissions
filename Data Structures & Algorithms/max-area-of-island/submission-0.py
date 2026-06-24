class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        max_island = 0

        def dfs(row,col):
            # if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row,col) in visited:
            #     return 0

            visited.add((row,col))
            neighbor_sum = 0

            for x,y in dirs:
                n_row, n_col = row + x, col + y
                if 0 <= n_row < ROWS and 0 <= n_col < COLS and (n_row,n_col) not in visited and grid[n_row][n_col] == 1:
                    neighbor_sum += dfs(n_row, n_col)

            return 1 + neighbor_sum



        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_island = max(dfs(row,col), max_island)
        return max_island

