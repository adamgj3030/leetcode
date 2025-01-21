class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        minCapital.sort()
        n = len(minCapital)
        i = 0
        
        for _ in range(k):
            while i < n and minCapital[i][0] <= w:
                heapq.heappush(maxProfit, -minCapital[i][1])
                i += 1

            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit)

        return w
