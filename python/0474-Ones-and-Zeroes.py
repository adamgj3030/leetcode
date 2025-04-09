class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        # dp holds a 2d mapping of (n + 1) and (m + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        nextdp = [[0] * (n + 1) for _ in range(m + 1)]

        for string in strs:
            zeros = string.count('0')
            ones = string.count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    nextdp[j][k] = dp[j][k] 
                    if j >= zeros and k >= ones:
                        nextdp[j][k] = max(dp[j][k], 1 + dp[j - zeros][k - ones])
            dp, nextdp = nextdp, dp

        return dp[m][n]
