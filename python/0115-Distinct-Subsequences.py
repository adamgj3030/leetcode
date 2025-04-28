'''
maximize distinct subsequences of s which are equal to t
dfs to look at every combination of subsequences in s and return how many of those equal t O(2^(s + t)) time
add memoization to make this a top down approach, O(s * t) time
bottom up base cases when j = 0, one way to make such a distinct subsequence
s = "caaat"
         ^
t = "cat"
       ^
res = 1 + ...
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        nextdp = [0] * (n + 1)
        for i in range(1, m + 1):
            dp[0] = 1
            for j in range(1, n + 1):
                nextdp[j] = dp[j]
                if s[i - 1] == t[j - 1]:
                    nextdp[j] += dp[j - 1]
            dp, nextdp = nextdp, dp
        return dp[n]
