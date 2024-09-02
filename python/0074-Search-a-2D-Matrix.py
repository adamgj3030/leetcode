class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, (len(matrix) - 1)

        while L <= R:
            mid = (L + R) // 2
            if target < matrix[mid][0]:
                R = mid - 1
            elif target > matrix[mid][-1]:
                L = mid + 1
            else:
                break

        if not (L <= R):
            return False
            
        listT = matrix[mid]
        L, R = 0, (len(listT) - 1)

        while L <= R:
            mid = (L + R) // 2
            if target < listT[mid]:
                R = mid - 1
            elif target > listT[mid]:
                L = mid + 1
            else:
                return True
        
        return False
