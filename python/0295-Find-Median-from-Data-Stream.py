class MedianFinder:

    def __init__(self):
        self.smallheap, self.largeheap = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap, -1 * num)
        if (self.smallheap) and (self.largeheap) and ((self.smallheap[0] * -1) > self.largeheap[0]):
            num = -1 * heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, num)
        
        if len(self.smallheap) > (len(self.largeheap) + 1):
            num = -1 * heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, num)
        
        elif len(self.largeheap) > (len(self.smallheap) + 1):
            num = heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap, -1 * num)
        

    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return (-1 * self.smallheap[0])
        if len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]
        return (((-1 * self.smallheap[0]) + self.largeheap[0]) / 2)
        
        
        
