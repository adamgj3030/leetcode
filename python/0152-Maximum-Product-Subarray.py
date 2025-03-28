class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = 1
        curMax = 1
        for n in nums:
            temp = curMin * n
            curMin = min(temp, curMax * n, n)
            curMax = max(temp, curMax * n, n)
            res = max(res, curMax)
        return res
