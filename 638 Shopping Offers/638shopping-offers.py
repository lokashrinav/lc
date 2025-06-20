class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        hmap = {}
        def dfs():

            if tuple(needs) in hmap:
                return hmap[tuple(needs)]

            minCost = 0
            for i in range(len(needs)):
                minCost += needs[i] * price[i]

            for i in range(len(special)):
                flag = True
                for p in range(len(needs)):
                    if needs[p] < special[i][p]:
                        flag = False
                    
                if flag:
                    for p in range(len(needs)):
                        needs[p] -= special[i][p]
                
                    minCost = min(minCost, special[i][-1] + dfs())

                    for p in range(len(needs)):
                        needs[p] += special[i][p]
            
            hmap[tuple(needs)] = minCost
                
            return minCost
        
        return dfs()