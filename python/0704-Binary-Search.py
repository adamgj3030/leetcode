class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or (len(nums) == 0):
            return -1
        
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
        
        return -1
