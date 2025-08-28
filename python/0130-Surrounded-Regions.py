class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visit = set()

        def dfs(r: int, c: int) -> None:
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r, c) in visit or board[r][c] == "X"
                ):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return

        for r in (0, rows - 1):
            for c in range(cols):
                dfs(r, c)
        for c in (0, cols - 1):
            for r in range(1, rows - 1):
                dfs(r, c)
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if (r, c) not in visit:
                    board[r][c] = "X"
