class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        currRow = [0] * cols
        currRow[cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                elif (c + 1) < cols:
                    currRow[c] += currRow[c + 1]

        return currRow[0]
