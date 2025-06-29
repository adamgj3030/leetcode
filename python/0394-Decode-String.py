'''
3[a2[c]]

res = ""
we push everything onto the stack until we see a ]
    stack = [3, [, a, 2, [, c]
Add to a cur string until we see a [ 
    stack = [3, [, a, 2]
    curString = c
Add to a repeatNum until we dont see a digit anymore
    stack = [3, [, a]
    curString = c
    repeatNum = 2
curString = "c" * repeatNum
          = "c" * 2
          = "cc"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                curString = ""
                while stack[-1] != '[':
                    curString = stack.pop() + curString
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(curString * int(k))
            else:
                stack.append(char)
        return "".join(stack)


OR


'''
3[a]2[bc]

use stack and constantly track information in []
do this by tracking before [ and then changing stack when we see a ]

track stack, cur_num, and cur_string
iterate through s
    if char is '['
        push cur_num and cur_string to stack and reset
    elif char is ']'
        pop cur_num and prev_string from stack
        cur_string is not prev_string + (cur_num * cur_string)
    elif char is a num:
        cur_num = char + cur_num
    else:
        cur_string = char + cur_string
return cur_string
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ""
        cur_num = 0

        for char in s:
            if char == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ""
                cur_num = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + (num * cur_string)
            elif char.isdigit():
                cur_num = (cur_num * 10) + int(char)
            else:
                cur_string += char
        
        return cur_string
