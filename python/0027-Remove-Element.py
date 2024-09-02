class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0

        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1
        return L
