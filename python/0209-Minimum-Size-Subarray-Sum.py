class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        L = 0
        currSum = 0

        for R in range(len(nums)):
            currSum += nums[R]
            while currSum >= target:
                currLength = R - L + 1
                if currLength < length:
                    length = currLength
                currSum -= nums[L]
                L += 1
        if length > len(nums):
            return 0
        return length
