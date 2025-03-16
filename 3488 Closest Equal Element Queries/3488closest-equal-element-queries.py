class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        '''
        0, 2, 4
        '''

        hmap = defaultdict(list)

        for i, num in enumerate(nums):
            hmap[num].append(i)
            
        res = {}

        for num in hmap:
            if len(hmap[num]) == 1:
                res[hmap[num][0]] = -1
                continue
            if len(hmap[num]) == 2:
                calc = min(abs(hmap[num][0] - hmap[num][1]), abs(hmap[num][0] + (len(nums) - hmap[num][1])))
                res[hmap[num][0]] = calc
                res[hmap[num][1]] = calc
                continue
            for ind in range(len(hmap[num])):
                if ind == 0:
                    diff1 = len(hmap[num]) - 1
                else:
                    diff1 = ind - 1

                if ind + 1 == len(hmap[num]):
                    diff2 = 0
                else:
                    diff2 = ind + 1

                if diff1 < ind:
                    calc1 = min(abs(hmap[num][ind] - hmap[num][diff1]), abs(hmap[num][diff1] + (len(nums) - hmap[num][ind])))
                else:
                    calc1 = min(abs(hmap[num][ind] - hmap[num][diff1]), abs(hmap[num][ind] + (len(nums) - hmap[num][diff1])))
                
                if diff2 < ind:
                    calc2 = min(abs(hmap[num][ind] - hmap[num][diff2]), abs(hmap[num][diff2] + (len(nums) - hmap[num][ind])))
                else:
                    calc2 = min(abs(hmap[num][ind] - hmap[num][diff2]), abs(hmap[num][ind] + (len(nums) - hmap[num][diff2])))

                if calc1 < calc2:
                    res[hmap[num][ind]] = calc1
                else:
                    res[hmap[num][ind]] = calc2
        print(res)
        for i in range(len(queries)):
            queries[i] = res[queries[i]]

        return queries
                

        