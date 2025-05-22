class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        '''
        10, 
        70, 
        350,
        10
        '''

        n = len(costs) // 2

        for i in range(len(costs)):
            costs[i] = (-1 * abs(costs[i][0] - costs[i][1]), costs[i][0], costs[i][1])
        
        heapify(costs)

        first, second = 0, 0
        total = 0

        while costs:
            diff, cost1, cost2 = heappop(costs)
            if (cost1 < cost2 and first < n) or second >= n:
                first += 1
                total += cost1
            else:
                second += 1
                total += cost2
        
        return total

            





        