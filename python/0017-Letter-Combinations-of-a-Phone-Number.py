class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []
        if not digits:
            return res
        
        def backtrack(i: int, curStr: str) -> None:
            if i >= len(digits):
                res.append(curStr)
                return
            for char in numToChar[digits[i]]:
                backtrack(i + 1, curStr + char)

        backtrack(0, "")
        return res

