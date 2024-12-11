class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = nums[0]
        for i in range(1, n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = nums[-1]
        for i in range(n - 2, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
