# Recursive (Top-down) approach with memoization
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # needed to access nums in other functions
        self.nums = nums
        # Initialize the minProd, maxProd, and dp arrays for memoization
        self.minProd = [None] * n
        self.maxProd = [None] * n
        self.dp = [None] * n
        # Set the base cases for each array
        self.minProd[0] = self.maxProd[0] = self.dp[0] = nums[0]
        # Return the recursive function for the original problem, n
        return self.dpRec(n - 1)
    

    def minProdRec(self, i) -> int:
        # If not currently stored, calculate it
        if self.minProd[i] is None:
            # Second recursive formulation
            self.minProd[i] = min(
                self.minProdRec(i - 1) * self.nums[i],
                self.maxProdRec(i - 1) * self.nums[i],
                self.nums[i])
        return self.minProd[i]


    def maxProdRec(self, i) -> int:
        # If not currently stored, calculate it
        if self.maxProd[i] is None:
            # Third recursive formulation
            self.maxProd[i] = max(
                self.minProdRec(i - 1) * self.nums[i],
                self.maxProdRec(i - 1) * self.nums[i],
                self.nums[i])
        return self.maxProd[i]


    def dpRec(self, i: int) -> int:
        # If not currently stored, calculate it
        if self.dp[i] is None:
            # First recursive formulation
            self.dp[i] = max(self.dpRec(i - 1), self.maxProdRec(i))
        return self.dp[i]





class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = 1
        curMax = 1
        for n in nums:
            temp = curMin * n
            curMin = min(temp, curMax * n, n)
            curMax = max(temp, curMax * n, n)
            res = max(res, curMax)
        return res
