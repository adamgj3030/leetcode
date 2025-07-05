'''
push to stack the dates that dont have a 'warmer' temp yet
when we find a warmer temp than the stack, while loop backwards into the stack
works because stack will always hold decreasing temp days 
until we find an 'increase' temp day
track res and stack
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((temp, i))
        
        return res
