'''

'''
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        state = set()
        max_sum = 0
        cur_sum = 0

        for r in range(n):
            while nums[r] in state:
                state.discard(nums[l])
                cur_sum -= nums[l]
                l += 1
            
            state.add(nums[r])
            cur_sum += nums[r]

            if (r - l + 1) == k:
                max_sum = max(max_sum, cur_sum)
                state.discard(nums[l])
                cur_sum -= nums[l]
                l += 1
        
        return max_sum
