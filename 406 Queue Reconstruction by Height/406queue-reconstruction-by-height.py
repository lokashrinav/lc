class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
            7, 0 - 7, 1
        '''

        people.sort(key=lambda x:(-x[0], x[1]))

        res = []

        for pep in people:
            res.insert(pep[1], pep)
        
        return res

