class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        # total = 1 + 4 + 5 = 11

        count = 0
        preCount = 0
        total = 0
        res = []
        preTotal = 0

        for i in range(len(boxes)):
            if boxes[i] == "1":
                total += i
                count += 1

        for i in range(len(boxes)):
            if boxes[i] == "1":
                count -= 1
                preCount += 1
            res.append(total + preTotal)
            total -= count
            preTotal += preCount
        
        return res



