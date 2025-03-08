from collections import defaultdict
from typing import List

'''
create adjacency list for each prereq
hashmap of each node with a default of a set
each set will correspond to its prereqs
queries will use dfs to find all prereqs and fill up the corresponding set
queries will first check to see if hashmap is already set for said course, if not do dfs

'''
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        prereqMap = defaultdict(set)

        def dfs(crs: int) -> set:
            if crs in prereqMap:
                return prereqMap[crs]
            
            for pre in adj[crs]:
                prereqMap[crs].add(pre)
                prereqMap[crs] |= dfs(pre)

            return prereqMap[crs]

        res = []
        for pre, crs in queries:
            if crs in prereqMap:
                res.append(pre in prereqMap[crs])
            else:
                dfs(crs)
                res.append(pre in prereqMap[crs])

        print(prereqMap)
        return res
