class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten_oranges = deque([])
        orange_count = 0
        minute = -1

        def add_cell(row,col):
            nonlocal orange_count

            if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                rotten_oranges.append((row,col))
                grid[row][col] = 2
                orange_count -= 1 


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten_oranges.append((row,col))
                if grid[row][col] == 1:
                    orange_count += 1

        if orange_count == 0: return 0
        
        while rotten_oranges:
            rotten_count = len(rotten_oranges)

            for _ in range(rotten_count):
                orange = rotten_oranges.popleft()
                row, col = orange[0], orange[1]
                add_cell(row + 1,col)
                add_cell(row - 1,col)
                add_cell(row,col + 1)
                add_cell(row,col - 1)

            minute += 1

        return minute if orange_count == 0 else -1




