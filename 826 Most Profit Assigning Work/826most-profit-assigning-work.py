class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        arr = [[difficulty[i], profit[i]] for i in range(len(profit))]
        arr.sort()

        difficulty = [arr[i][0] for i in range(len(profit))]
        profit = [arr[i][1] for i in range(len(profit))]

        maxProfit = profit[0]
        for i in range(1, len(profit)):
            if maxProfit > profit[i]:
                profit[i] = maxProfit
            else:
                maxProfit = profit[i]

        worker.sort()

        ind = len(worker) - 1
        total = 0

        #print(difficulty, profit, worker)

        for i in range(len(difficulty) - 1, -1, -1):
            while ind >= 0 and worker[ind] >= difficulty[i]:
                total += profit[i]
                ind -= 1
        
        return total

            
        