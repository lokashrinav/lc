class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        res = []
        for i in range(len(names)):
            res.append((names[i], heights[i]))

        res = sorted(res, key=lambda x:(-x[1], x[0]))

        return [elem[0] for elem in res]