class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(1, ROWS + 1):
            prevTotal = 0
            for c in range(1, COLS + 1):
                above = self.prefixMatrix[r - 1][c]
                prevTotal += matrix[r - 1][c - 1]
                self.prefixMatrix[r][c] = prevTotal + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixMatrix[row2][col2]
        left = self.prefixMatrix[row2][col1 - 1]
        top = self.prefixMatrix[row1 - 1][col2]
        topLeft = self.prefixMatrix[row1 - 1][col1 - 1]
        
        return bottomRight + topLeft - (left + top)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
