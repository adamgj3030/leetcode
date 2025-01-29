class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # initialize a minHeap with starting position and elevation
        # use a visited set to track visisted squares
        # while minHeap is not empty
        # - pop the lowest avaliable elevation from the current path
        # - check if we have reach the bottom right
        # - explore all possible neighbors
        # - push valid (not visited, in bounds) neighbors to minHeap 
        # return maximum elevation encountered

        n = len(grid)
        visit = set()
        res = grid[0][0]

        # elevation, row, col
        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            elv, r, c = heapq.heappop(minHeap)
            visit.add((r, c))
            res = max(res, elv)
            if r == n - 1 and c == n - 1:
                return res
            adj = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for ar, ac in adj:
                if not (0 <= ar < n and 0 <= ac < n) or (ar, ac) in visit:
                    continue
                heapq.heappush(minHeap, (grid[ar][ac], ar, ac))
        return -1

            
