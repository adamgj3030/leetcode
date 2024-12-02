class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L1, R1 = 0, 0
        L2, R2 = 0, 0
        length1, length2 = 0, 0
        maxLength = 1

        for i in range(len(arr) - 1):
            # when index is even
            if (i % 2) == 0:
                # handle case 1
                if arr[i] < arr[i + 1]:
                    R1 += 1
                    length1 = (R1 - L1) + 1
                else:
                    length1 = (R1 - L1) + 1
                    L1, R1 = i, i

                # handle case 2
                if arr[i] > arr[i + 1]:
                    R2 += 1
                    length2 = (R2 - L2) + 1
                else:
                    length2 = (R2 - L2) + 1
                    L2, R2 = i, i

            # when index is odd
            else:
                # handle case 1
                if arr[i] > arr[i + 1]:
                    R1 += 1
                    length1 = (R1 - L1) + 1
                else:
                    length1 = (R1 - L1) + 1
                    L1, R1 = i, i

                # handle case 2
                if arr[i] < arr[i + 1]:
                    R2 += 1
                    length2 = (R2 - L2) + 1
                else:
                    length2 = (R2 - L2) + 1
                    L2, R2 = i, i
            tempMax = max(length1, length2)
            maxLength = max(maxLength, tempMax)
        return maxLength
