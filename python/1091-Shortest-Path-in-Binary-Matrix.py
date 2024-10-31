class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # no rows or cols
        if not grid or not grid[0]:
            return -1

        if grid[0][0] == 1:
            return -1    

        rows, cols = len(grid), len(grid[0])
        #breadth first search
        def bfs(grid):
            # holds the already visited positions
            visit = set()
            # holds the next breadth of positions
            queue = deque()

            # start at (0, 0)
            visit.add((0, 0))
            queue.append((0, 0))

            length = 1
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if (r == rows - 1) and (c == cols - 1):
                        return length
                    
                    # 4 edges and 4 corners
                    direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

                    for dr, dc in direction:
                        #new r and new c
                        nr, nc = r + dr, c + dc
                        #skip if out of bounds, already visited, or = 1
                        if (nr < 0 or nc < 0 or
                            nr == rows or nc == cols or
                            ((nr, nc) in visit) or (grid[nr][nc] == 1)
                            ):
                            continue

                        visit.add((nr, nc))
                        queue.append((nr, nc))
                length += 1
            return -1

        length = bfs(grid)

        return length
