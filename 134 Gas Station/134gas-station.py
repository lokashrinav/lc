class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        currGas = 0
        start = 0
        for i in range(len(cost)):
            currGas += (gas[i] - cost[i])
            if currGas < 0:
                start = i + 1
                currGas = 0
        if currGas == 0 and start == len(cost):
            return -1
        else:
            return start





        