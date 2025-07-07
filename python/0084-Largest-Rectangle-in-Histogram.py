'''
track a stack and max_rec
iterate i and h through enumeratedheights,
    lowest_i = i
    while stack and h < stack[-1]:
        j, past_h = stack.pop()
        cur_rec = past_h * (i - j)
        max_rec = max(max_rec, cur_rec)
        lowest_i = j
    stack.append((lowest_i, h))

while stack:
    j, past_h = stack.pop()
    cur_rec = past_h * (i - j)
    max_rec = max(max_rec, cur_rec)

return max_rec

'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_rec = 0
        for i, h in enumerate(heights):
            lowest_i = i
            while stack and h < stack[-1][1]:
                j, past_h = stack.pop()
                cur_rec = past_h * (i - j)
                max_rec = max(max_rec, cur_rec)
                lowest_i = j
            stack.append((lowest_i, h))

        while stack:
            j, past_h = stack.pop()
            cur_rec = past_h * (n - j)
            max_rec = max(max_rec, cur_rec)

        return max_rec
