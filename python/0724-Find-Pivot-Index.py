class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        leftSum = 0

        for i, n in enumerate(nums):
            rightSum = total - (leftSum + n)
            if rightSum == leftSum:
                return i
            leftSum += n
        return -1
