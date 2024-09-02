class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = {0 : 0, 1 : 0}

        for s in students:
            count[s] += 1
        
        for s in sandwiches:
            if count[s] <= 0:
                return res

            count[s] -= 1
            res -= 1

        return res
