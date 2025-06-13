class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        '''

        -2, 1, -4, 6, -4

        -12,-9,-3,-12,-6

        -3, -6, -9, -12, -12

        '''
        res = []
        for p in range(len(l)):
            new = nums[l[p]:r[p]+1]
            new.sort()
            saved = None
            flag = True if len(new) >= 2 else False
            for i in range(len(new) - 1):
                if saved is None:
                    saved = new[i + 1] - new[i] 
                else:
                    if new[i + 1] - new[i] == saved:
                        continue
                    else:
                        flag = False
                
                #print(p, new, new[i + 1], new[i], flag)
            
            res.append(flag)
        
        return res


        