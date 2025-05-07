'''
Minimize operations (Insert, Delete, Replace) on word 1 to match word 2
Naive approach is to do a dfs approach where we check every possible operation
at every position, which takes O(3^n) where n is the max length of word1 or word2
Add memoization to make this a top-down approach which takes O(n^2)
Bottom-up uses same memoization table, base case is when i/j = 0, dp is just 
word1/word2 - i/j.
        m   o   n   e   y
    0   1   2   3   4   5
m   1   
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 > n2:
            n1, n2 = n2, n1
            word1, word2 = word2, word1
        dp = [0] * (n2 + 1)
        nextdp = [0] * (n2 + 1)
        for j in range(n2 + 1):
            dp[j] = j
        for i in range(1, n1 + 1):
            nextdp[0] = i
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    nextdp[j] = dp[j - 1]
                else:
                    nextdp[j] = min(
                        dp[j],
                        nextdp[j - 1],
                        dp[j - 1]
                    ) + 1
            dp, nextdp = nextdp, dp
        return dp[n2]
