class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]),
                        max(newInterval[1], intervals[i][1])]
            i += 1
        
        merged.append(newInterval)
        while i < n:
            merged.append(intervals[i])
            i += 1
        
        return merged
