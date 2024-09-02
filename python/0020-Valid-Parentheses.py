class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = { ")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if char in hashMap:
                if stack and (stack[-1] == hashMap[char]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
    
        if not stack:
            return True
        return False
