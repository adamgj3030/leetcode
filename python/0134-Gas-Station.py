class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        def dfs(i, tank, station):
            if station == n:
                return True
            tank += gas[i] - cost[i]
            if tank < 0:
                return False
            return dfs((i + 1) % n, tank, station + 1)

        for i in range(n):
            if dfs(i, 0, 0):
                return i
        return -1
