class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            while (numbers[L] + numbers[R]) > target:
                R -= 1
            while (numbers[L] + numbers[R]) < target:
                L += 1
            if (numbers[L] + numbers[R]) == target:
                return [L + 1, R + 1]
