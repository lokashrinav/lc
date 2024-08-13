class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
            if len(hmap.keys()) >= 3:
                saved = list(hmap.keys())
                for i in range(len(hmap.keys())):
                    elem = saved[i]
                    hmap[elem] -= 1
                    if hmap[elem] == 0:
                        del hmap[elem]

        list1 = []
        for elem in hmap.keys():
            if nums.count(elem) > (len(nums) // 3):
                list1.append(elem)

        return list1
                        


            

        
        # 1, 2, 3, 1, 2, 4

        