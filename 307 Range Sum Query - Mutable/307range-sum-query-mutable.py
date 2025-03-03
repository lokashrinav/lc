class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(self.nums)

        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = self.nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
        
    def update(self, index: int, val: int) -> None:
        pos = index + self.n
        self.tree[pos] = val
        pos //= 2

        while pos >= 1:
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
            pos //= 2
                
    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n

        s = 0
        
        while left <= right:
            if left % 2 == 1:
                s += self.tree[left]
                left += 1
            if right % 2 == 0:
                s += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        
        return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)