class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        '''
    


        1: 1
        0: 0
        count = 1
        # If we reach a 1, we add 1

        1: 1
        0: 1
        count = 2
        # If we reach a 0, we add count(1)

        1: 2
        0: 1
        count = 4
        # If we reach a 1 after we reach 1, we add count(0) + count(1) // 2 + 1

        1: 2
        0: 2
        count = 6
        
        '''

        '''

        1 1 1 1 1
        1 0 1 0 1

        '''

        prefix = 0
        count = 0
        hmap = defaultdict(int)
        hmap[0] = 1
        for elem in arr:
            prefix = (prefix + elem) % 2
            if prefix == 0:
                count += hmap[1]
                hmap[0] += 1
            else:
                count += hmap[0]
                hmap[1] += 1       

        return count % (10 ** 9 + 7)

        '''
        1 1 1

        '''


        