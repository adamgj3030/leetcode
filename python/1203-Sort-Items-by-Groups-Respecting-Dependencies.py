from typing import List
from collections import defaultdict

class Solution:
    '''
    Assign each item with group -1 to a new group m and increment m
    Create an adj list for beforeItems such that beforeItem i -> item i
        Check if any beforeItems are in a different group then its corresponding item
        if so, create an adj list for group such that group beforeItem i -> group item i
    Toposort for beforeItems and groups adj list
    Create an adj list to hold group j -> item i
    Add each beforeItem toposort to its corresponding group
    Add each groups toposort group to the resulting array
    return array
    '''
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i, grp in enumerate(group):
            if grp == -1:
                group[i] = m
                m += 1
        
        itmAdj = defaultdict(list)
        grpAdj = defaultdict(list)
        for i in range(n):
            for prev in beforeItems[i]:
                itmAdj[prev].append(i)
                if group[i] != group[prev]:
                    grpAdj[group[prev]].append(group[i])


        itmOrd = self.topoSort(n, itmAdj)
        if not itmOrd: return []
        grpOrd = self.topoSort(m, grpAdj)
        if not grpOrd: return []

        grpItms = defaultdict(list)
        for itm in itmOrd:
            grpItms[group[itm]].append(itm)
        
        res = []
        for grp in grpOrd:
            res.extend(grpItms[grp])
        
        return res


    '''
    Create an array of n 0's
    0 means unvisited
    1 means visiting
    2 means fully visited
    visit each number from 0 to n, true means cycle, false no cycle
        check if its already been fully visited (2):
            return False
        check if its already been visited (1):
            return True
        mark as visiting (1)
        check adj list nodes
        if any return True, we return True
        mark node as fully visited
        add to topolist
        return False
    call dfs func, if True, return []
    return topoList reversed
    '''    
    def topoSort(self, n: int, adj: DefaultDict[int, List[int]]) -> List[int]:
        res = []
        visit = [0] * n
        def dfs(node: int) -> bool:
            if visit[node] == 1:
                return True
            elif visit[node] == 2:
                return False
            
            visit[node] = 1
            for nei in adj[node]:
                if dfs(nei):
                    return True
            
            visit[node] = 2
            res.append(node)
            return False

        for i in range(n):
            if dfs(i):
                return []
        return res[::-1]
