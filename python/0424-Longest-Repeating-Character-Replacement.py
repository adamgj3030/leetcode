class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxLength = 0
        count = {}

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)

            while (R - (L - 1) - max(count.values())) > k:
                count[s[L]] -= 1
                L += 1

            maxLength = max(maxLength, R - (L - 1))
        return maxLength
