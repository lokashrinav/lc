class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        for i in range(len(boxTypes)):
            boxTypes[i] = [-boxTypes[i][1], -boxTypes[i][0]]
        
        heapify(boxTypes)

        sum1 = 0
        while boxTypes and truckSize:
            units, boxes = heappop(boxTypes)
            units = -units
            boxes = -boxes

            if boxes >= truckSize:
                sum1 += units * truckSize
                truckSize = 0
            else:
                sum1 += units * boxes
                truckSize -= boxes

        return sum1
            
        