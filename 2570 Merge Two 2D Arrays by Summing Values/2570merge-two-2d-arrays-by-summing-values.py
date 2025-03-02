class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ind1, ind2 = 0, 0

        arr = []
        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1][0] == nums2[ind2][0]:
                arr.append([nums1[ind1][0], nums1[ind1][1] + nums2[ind2][1]])
                ind1 += 1
                ind2 += 1
            elif nums1[ind1][0] > nums2[ind2][0]:
                arr.append([nums2[ind2][0], nums2[ind2][1]])
                ind2 += 1
            else:
                arr.append([nums1[ind1][0], nums1[ind1][1]])
                ind1 += 1
        

        while ind1 < len(nums1):
            arr.append([nums1[ind1][0], nums1[ind1][1]])
            ind1 += 1
        
        while ind2 < len(nums2):
            arr.append([nums2[ind2][0], nums2[ind2][1]])
            ind2 += 1
            
        return arr
