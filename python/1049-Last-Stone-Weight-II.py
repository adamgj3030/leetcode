class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        stoneSum = sum(stones)
        target = stoneSum // 2
        dp = [0] * (target + 1)
        nextdp = [0] * (target + 1)
        for stone in stones:
            for t in range(0, target + 1):
                if t >= stone:
                    nextdp[t] = max(dp[t], dp[t - stone] + stone)
                else:
                    nextdp[t] = dp[t]
            dp, nextdp = nextdp, dp
        return abs(stoneSum - (2 * dp[target]))
