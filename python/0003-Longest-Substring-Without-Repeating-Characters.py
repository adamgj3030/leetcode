class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        currChars = set()
        maxLength = 0
        
        for R in range(len(s)):
            while s[R] in currChars:
                currChars.remove(s[L])
                L += 1
            maxLength = max(maxLength, R - (L - 1))
            currChars.add(s[R])
        return maxLength
