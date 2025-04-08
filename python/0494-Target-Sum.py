from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        
        for i in range(1, n):
            nextdp = defaultdict(int)
            for curSum, count in dp.items():
                nextdp[curSum + nums[i]] += count
                nextdp[curSum - nums[i]] += count
            dp = nextdp

        return dp[target]
