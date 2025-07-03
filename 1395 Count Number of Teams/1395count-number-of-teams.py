class Solution:
    def numTeams(self, rating: List[int]) -> int:

        '''



        '''
        res = []
        for i in range(len(rating)):
            count = 0
            for p in range(i + 1, len(rating)):
                if rating[p] > rating[i]:
                    count += 1
            res.append(count)

        total = 0
        for i in range(len(rating)):
            for p in range(i + 1, len(rating)):
                if rating[p] > rating[i]:
                    total += res[p]

        res = []
        for i in range(len(rating)):
            count = 0
            for p in range(i + 1, len(rating)):
                if rating[p] < rating[i]:
                    count += 1
            res.append(count)

        for i in range(len(rating)):
            for p in range(i + 1, len(rating)):
                if rating[p] < rating[i]:
                    total += res[p]
        
        return total






        