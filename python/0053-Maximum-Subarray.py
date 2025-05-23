class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum = num + max(currSum, 0) 
            maxSum = max(maxSum, currSum)
        return maxSum
