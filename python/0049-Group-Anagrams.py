class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: Dict[Tuple[int], List[str]] = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            tupleCount = tuple(count)
            if tupleCount  in result:
                result[tupleCount].append(s)
            else:
                result[tupleCount] = [s]

        return list(result.values())
        
           
