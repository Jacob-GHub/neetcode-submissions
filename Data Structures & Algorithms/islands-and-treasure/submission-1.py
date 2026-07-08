class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(r,c):
            Q = deque()
            Q.append((r,c))
            visited = set((r,c))
            depth = 1

            while Q:
                num_layer = len(Q)
                for i in range(num_layer):
                    cur_r,cur_c = Q.popleft()
                    visited.add((cur_r,cur_c))
                    for x,y in directions:
                        n_row,n_col = cur_r + x, cur_c + y
                        if 0 <= n_row < ROWS and 0 <= n_col < COLS and grid[n_row][n_col] > 0 and (n_row,n_col) not in visited:
                            grid[n_row][n_col] = min(grid[n_row][n_col],depth)
                            Q.append((n_row,n_col))
                depth+=1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r,c)

