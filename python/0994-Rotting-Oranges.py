class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                destination = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in destination:
                    #new col, new row
                    nr, nc = r + dr, c + dc
                    if  (nr < 0 or nc < 0 or
                        nr == rows or nc == cols or
                        (nr, nc) in visit or grid[nr][nc] == 0
                        ):
                        continue
                    fresh -= 1
                    visit.add((nr, nc))
                    queue.append((nr, nc))

            time += 1

        if fresh != 0:
            return -1
        return time


