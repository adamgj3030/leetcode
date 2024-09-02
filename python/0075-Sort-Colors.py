class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        L, R = (0), (len(nums) - 1)
        i = 0

        while i <= R:
            if nums[i] == 0:
                swap(i, L)
                L += 1
            if nums[i] == 2:
                swap(i, R)
                R -= 1
                i -= 1
            i += 1
