class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #no rows or no columns
        if not grid or not grid[0]:
            return 0
        
        # will keep track of 'visited' islands
        visit = set()

        islands = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # if out of bounds, already visited, or '0', skip
            if  (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r, c) in visit or
                grid[r][c] == '0'
            ):
                return 0
            
            # plot has been visited
            visit.add((r, c))

            # check surrounding plots
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return 1
        
        for r in range(ROWS):
            for c in range(COLS):
                #only 'visit' the islands that have a '1' and havent been visited yet
                if (grid[r][c] == '1') and ((r, c) not in visit):
                    islands += dfs(r, c)
        return res
