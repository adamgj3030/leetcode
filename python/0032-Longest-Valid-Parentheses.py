'''
track a stack and max_len
if stack[-1] is ')'
    if stack[-1] is '('
    max_len = max(max_len, i - stack[-1])
else:
    append
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # ")()())"
        # stack = [(-1, None), (1, '('), ]
        # max_len = 0
        stack = [(-1, None)]
        max_len = 0
        for i, char in enumerate(s):
            if char == ')':
                if not stack:
                    stack = [(i, None)]
                if stack[-1][1] == '(':
                    stack.pop()
                    max_len = max(max_len, i - stack[-1][0])
                else:
                    stack.append((i, char))
            else:
                stack.append((i, char))
        return max_len
