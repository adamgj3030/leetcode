class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l = 0 
        r = n - k
        cur_sum = sum(cardPoints[r:])
        max_sum = cur_sum
        
        while r < n:
            cur_sum += (cardPoints[l] - cardPoints[r])
            max_sum = max(max_sum, cur_sum)
            r += 1
            l += 1
        
        return max_sum
