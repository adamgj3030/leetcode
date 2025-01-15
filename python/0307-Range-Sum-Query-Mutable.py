class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        self.buildTree(1, nums)
    
    def buildTree(self, i: int, nums: List[int]):
        if i >= self.n:
            self.tree[i] = nums[i - self.n]
            return
        self.buildTree((2 * i), nums)
        self.buildTree((2 * i) + 1, nums)

        self.tree[i] = self.tree[(2 * i)] + self.tree[(2 * i) + 1]
        

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val

        while index > 1:
            left = right = index
            if index % 2 == 0:
                right += 1
            else:
                left -= 1
            index //= 2
            self.tree[index] = self.tree[left] + self.tree[right] 
        

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        res = 0

        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
