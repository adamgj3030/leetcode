'''
need to minimize total coins while getting to amount
For every coin, keep (and try more of said coin) or skip.
use dfs to explore every coin combination for O(n^t)
add a cache/memoization so dfs doesnt repeat same subproblems for O(n * amount)
bottom up base case when amount = 0, coins = 0.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0

        for a in range(1, (amount + 1)):
            for coin in coins:
                if a >= coin:
                    memo[a] = min(memo[a], memo[a - coin] + 1)
        return memo[amount] if memo[amount] != float('inf') else -1
