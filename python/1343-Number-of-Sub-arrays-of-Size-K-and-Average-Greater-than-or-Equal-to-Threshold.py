class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        R = k - 1
        currSum = sum(arr[0:k - 1])
        target = k * threshold
        res = 0

        while R < len(arr):
            currSum += arr[R]
            if currSum >= target:
                res += 1
            currSum -= arr[R + 1 - k]
            R += 1
        return res
