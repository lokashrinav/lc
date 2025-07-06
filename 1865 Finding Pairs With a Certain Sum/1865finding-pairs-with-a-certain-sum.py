class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        adding = defaultdict(int)
        self.hmap = defaultdict(int)
        self.nums1 = nums1
        self.nums2 = nums2
        for i in range(len(nums2)):
            self.hmap[nums2[i]] += 1
        
    def add(self, index: int, val: int) -> None:
        self.hmap[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.hmap[self.nums2[index]] += 1
            
    def count(self, tot: int) -> int:
        total = 0
        for i in range(len(self.nums1)):
            if tot - self.nums1[i] in self.hmap:
                total += self.hmap[tot - self.nums1[i]]
        return total
            

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)