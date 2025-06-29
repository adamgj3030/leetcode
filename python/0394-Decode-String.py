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
