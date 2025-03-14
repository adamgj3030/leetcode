from typing import List
from collections import defaultdict

class Solution:
    '''
    Keep track of the indegree for every character in words
    Create adj list where a -> b means a comes before b in the 'dictionary'
    if we ever find more letters in word 1 than word 2 and everything before is the same, return ""
    find a -> b by comparing 2 adjacent words, iterating through each character until we find a differing char
    char difference will be first word char a -> second word char b
    topo sort to find resulting dictionary
    '''
    def foreignDictionary(self, words: List[str]) -> str:
        inDegree = defaultdict(int)
        for word in words:
            for c in word:
                if c not in inDegree:
                    inDegree[c] = 0

        cAdj = defaultdict(list)
        n = len(words)
        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    cAdj[w1[j]].append(w2[j])
                    inDegree[w2[j]] += 1
                    break

        letters = ''.join(inDegree.keys())
        res = self.topoSort(cAdj, inDegree)
        return res

    '''
    Kahns Algorithm
    Keep track of in degree level (how many parents said node has)
    if in degree is 0, then add it to the res and decrease in in degree of its children
    if the new in degree of its children is 0, add it to the q to be added later
    if the length of the resulting string isnt the same as the inDegree dict, we have a loop, return ""
    '''
    def topoSort(self, adj: defaultdict[str, List[str]], inDegree: defaultdict[int, int]) -> str:
        res = ""
        n = len(inDegree)
        q = deque([c for c in inDegree if inDegree[c] == 0])

        while q:
            cur = q.popleft()
            res += cur
            for nei in adj[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        if len(res) != n:
            return ""
        return res       
