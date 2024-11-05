class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        houses = len(nums)
        if houses == 1:
            return nums[0]
        h1 = nums[0]
        h2 = max(h1, nums[1])

        for i in range(2, houses):
            temp = h2
            h2 = max(nums[i] + h1, h2)
            h1 = temp
        return max(h1, h2)
