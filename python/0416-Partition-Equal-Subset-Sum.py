# TOP DOWN
# dfs function checks all possible partitions by checking:
# at every index i we can either put that num in partition 1 or partition 2

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def dfs(i: int, part1: int, part2: int) -> bool:
            if i == n:
                if part1 == part2:
                    return True
                return False

            if (i, part1, part2) in memo:
                return memo[(i, part1, part2)]

            part1 += nums[i]
            memo[(i + 1, part1, part2)] = dfs(i + 1, part1, part2)
            if memo[(i + 1, part1, part2)]:
                return True
            part1 -= nums[i]

            part2 += nums[i]
            memo[(i + 1, part1, part2)] = dfs(i + 1, part1, part2)
            if memo[(i + 1, part1, part2)]:
                return True
            part2 -= nums[i]

            return False
        
        if dfs(0, 0, 0):
            return True
        return False


# BOTTOM UP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        nextDp = [False] * (target + 1)

        dp[0] = True 
        for i in range(len(nums)):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    nextDp[j] = dp[j] or dp[j - nums[i]]
                else:
                    nextDp[j] = dp[j]
            dp, nextDp = nextDp, dp
            
        return dp[target]
