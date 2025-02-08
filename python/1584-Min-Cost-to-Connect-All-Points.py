class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        minHeap = []
        for nei, dist in adj[0]:
            heapq.heappush(minHeap, (dist, nei))
        
        visit = set()
        visit.add(0)
        cost = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            cost += dist
            for nei, dist in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (dist, nei))
        return cost
