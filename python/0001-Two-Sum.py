class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        currMap = {}

        for i in range(len(nums)):
            currNum = nums[i]
            difference = target - currNum

            if (difference) in currMap:
                return [currMap[difference], i]
            
            currMap[currNum] = i
