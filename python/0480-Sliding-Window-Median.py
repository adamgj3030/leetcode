class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # small: max heap
        # large: min heap
        small, large = [], []
        # dict to keep track of nums to be removed from the window
        heapDict = defaultdict(int)

        for i in range(k):
            heapq.heappush(small, -nums[i])
        for i in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))
        
        res = [-small[0] if k & 1 else (large[0] - small[0]) / 2]
        for i in range(k, len(nums)):
            prevNum = nums[i - k]
            heapDict[prevNum] += 1
            # res[-1]: prev median
            # balance -1 if num to remove is in small, 1 for num in large
            balance = -1 if prevNum <= res[-1] else 1

            if nums[i] <= -small[0]:
                heapq.heappush(small, -nums[i])
                balance += 1
            else:
                heapq.heappush(large, nums[i])
                balance -= 1
            
            if balance < 0:
                heapq.heappush(small, -heapq.heappop(large))
            elif balance > 0:
                heapq.heappush(large, -heapq.heappop(small))
            
            while small and heapDict[-small[0]] > 0:
                heapDict[-heapq.heappop(small)] -= 1
            while large and heapDict[large[0]] > 0:
                heapDict[heapq.heappop(large)] -= 1

            res.append(-small[0] if k & 1 else (large[0] - small[0]) / 2)
        
        return res
