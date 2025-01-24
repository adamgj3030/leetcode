class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i: int, comb: List[int]) -> None:
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for j in range(i, n + 1):
                comb.append(j)
                backtrack(j + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res
