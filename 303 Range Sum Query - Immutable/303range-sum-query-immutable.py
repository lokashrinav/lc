class NumArray:

    def __init__(self, nums: List[int]):
        self.total = []
        for i in range(len(nums)):
            if not self.total:
                self.total.append(nums[i])
            else:
                self.total.append(self.total[-1] + nums[i])
        print(self.total)

    def sumRange(self, left: int, right: int) -> int:
        idk = self.total[left - 1] if left - 1 >= 0 else 0
        x = self.total[right] - idk
        return x
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)