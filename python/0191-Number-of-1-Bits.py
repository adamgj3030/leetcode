class Solution:
    def countBits(self, n: int) -> List[int]:
        cache = [0] * (n + 1)

        for num in range(n + 1):
            cache[num] = cache[num >> 1] + (num & 1)
        return cache
