class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))
        
        visit = set()
        minHeap = [(-1, start_node)]
        
        while minHeap:
            currProb, node = heapq.heappop(minHeap)
            if node == end_node:
                return -currProb
            visit.add(node)
            for nei, prob in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, ((prob * currProb), nei))
        return 0
