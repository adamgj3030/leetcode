from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        path = set()
        order = []
        
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            
            path.add(node)
            for child in adj[node]:
                if not dfs(child):
                    return False
            path.remove(node)
            visit.add(node)
            order.append(node)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        return order
