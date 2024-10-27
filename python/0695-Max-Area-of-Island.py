class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # no rows or columns(cols)
        if not grid or not grid[0]:
            return 0
        
        # keep track of max island area, visited areas, and size of rows and cols
        maxArea = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # if area is out of bounds, has been visited, or is = 0 return 0
            if  (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == 0
                ):
                return 0
            
            visit.add((r, c))

            count = 1
            destination = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in destination:
                count += dfs(r + dr, c + dc)
            
            return count
        
        for r in range(rows):
            for c in range(cols):
                # if area = 1 AND area hasnt been visited yet
                if (grid[r][c] == 1) and ((r, c) not in visit):
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea
