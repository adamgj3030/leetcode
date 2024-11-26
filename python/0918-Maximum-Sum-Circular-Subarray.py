class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, maxSum = 0, nums[0]
        currMin, minSum = 0, nums[0]
        

        for num in nums:
            currMax = max(currMax, 0)
            currMax += num
            currMin = min(currMin, 0)
            currMin += num
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
        if minSum == sum(nums):
            return maxSum
        wrappingSum = sum(nums) - minSum
        return max(wrappingSum, maxSum)
