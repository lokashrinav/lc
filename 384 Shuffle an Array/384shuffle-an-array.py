class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.shuffe = nums[:]

    def reset(self) -> List[int]:
        return self.nums            
        
    def shuffle(self) -> List[int]:
        for i in range(len(self.nums) - 1, 0, -1):
            num = random.randint(0, i)
            self.shuffe[i], self.shuffe[num] = self.shuffe[num], self.shuffe[i]
        return self.shuffe
        
        
        


                


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()