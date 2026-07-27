class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0],0,0)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set((0,0))
        max_elevation = 0
        n = len(grid)

        while min_heap:
            weight, i, j = heapq.heappop(min_heap)
            max_elevation = max(max_elevation, weight)

            if (i,j) == (n-1,n-1): 
                return max_elevation

            for x,y in directions:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < n and 0 <= new_j < n and (new_i,new_j) not in visited:
                    n_weight = max(grid[new_i][new_j], max_elevation)
                    heapq.heappush(min_heap,(n_weight,new_i,new_j))
                    visited.add((new_i,new_j))

        return max_elevation
