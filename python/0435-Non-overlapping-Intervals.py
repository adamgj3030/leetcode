'''
be greedy by finding non-overlapping intervals then n - res
sort by end time, then check if i[0] > i[1], means we found a non-overlapping interval
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        i = 1
        end = 0
        # res is the count of non-overlapping intervals
        res = 1

        for i in range(1, n):
            if intervals[end][1] <= intervals[i][0]:
                end = i
                res += 1
        
        return n - res
