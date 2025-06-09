'''
True if s3 can be interleaved from characters from s1 and s2
dfs to find if any interleaving works
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if len(s3) != (n + m):
            return False
        
        memo = {}
        def dfs(i: int, j: int) -> bool:
            if i == n and j == m:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            if i < n and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    memo[(i, j)] = True
                    return True
            if j < m and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    memo[(i, j)] = True
                    return True
            memo[(i, j)] = False
            return False
            
        return dfs(0, 0)
