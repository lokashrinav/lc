class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        
        hmap = defaultdict(int)
        count = defaultdict(int)
        res = []

        for i in range(len(queries)):
            if queries[i][0] in hmap:
                idk = hmap[queries[i][0]]
                count[idk] -= 1
                if count[idk] == 0:
                    del count[idk]

            hmap[queries[i][0]] = queries[i][1]
            count[queries[i][1]] += 1
            res.append(len(count))
        
        return res



        '''

        4 -> 1

        5 -> 2

        3 -> 1

        '''
