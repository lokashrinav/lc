class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        res = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] not in res:
                res[groupSizes[i]] = [[]]

            if len(res[groupSizes[i]][-1]) == groupSizes[i]:
                res[groupSizes[i]].append([])

            res[groupSizes[i]][-1].append(i)
        
        final = []

        for key, val in res.items():
            for elem in val:
                if elem:
                    final.append(elem)

        return final           
        