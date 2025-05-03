class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        stack = []
        hmap = defaultdict(int)
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                hmap[nums2[i]] = stack[-1]
            else:
                hmap[nums2[i]] = -1

            stack.append(nums2[i])
        
        print(hmap)

        res = []
        for i in range(len(nums1)):
            res.append(hmap[nums1[i]])
        
        return res