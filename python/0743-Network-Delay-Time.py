class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        # s is source, d is destination, w is weight
        for s, d, w in times:
            adj[s].append((w, d))
        
        shortest = {}
        minHeap = [(0, k)]
        maxTime = 0
        while minHeap:
            w1, d1 = heapq.heappop(minHeap)
            if d1 in shortest:
                continue
            shortest[d1] = w1
            maxTime = max(maxTime, w1)

            for w2, d2 in adj[d1]:
                if d2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, d2))
        
        if len(shortest) != n:
            return -1

        return maxTime
