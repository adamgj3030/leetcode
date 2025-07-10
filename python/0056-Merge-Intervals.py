'''
SORT FIRST
keep a new array merged to track currently non-overlapping intervals
if we find an interval (merged[-1][1] > intervals[i][0]) end of the time is > start of the next time
then merge the two intervals (merged[-1][1] = intervals[i][1])
return merged list
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
