class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        res = [1] * len(ratings)
        curr = 1
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                res[i + 1] = res[i] + 1
        
        #print(res) 
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                res[i - 1] = max(res[i - 1], res[i] + 1)
        
        #print(res)

        return sum(res)