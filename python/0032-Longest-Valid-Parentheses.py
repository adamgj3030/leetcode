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



OR



'''
'greedily' use left and right pointers to track longest
right tracks ')' and left tracks '('
if right is ever > left, we know the the longest possible has stopped growing
reset and continue
when they match, we have '(' == ')' and can see if there is a new max_len
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0

        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif left > right:
                left = right = 0
        
        return max_len
            
