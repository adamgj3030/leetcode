class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # ensures that the variable text2 is the shortest
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        size1, size2 = len(text1), len(text2)
        
        prev = [0] * (size2 + 1)
        
        for L in range(size1 - 1, -1, -1):
            curr = [0] * (size2 + 1)
            for R in range(size2 - 1, -1, -1):
                if text1[L] == text2[R]:
                    curr[R] = 1 + prev[R + 1]
                else:
                    curr[R] = max(curr[R + 1], prev[R])
            prev = curr             

        return curr[0]
