class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        # 2, 1, 1, 2, 1

        '''

        2, 1

        2, 3

        3, 5

        5, 4

        '''

        p1, p2 = 0, 1
        bestNum = None
        count = 0
        fun = 0

        while True:
            fun += 1
            if p1 >= len(arr) or p2 >= len(arr):
                return bestNum

            maxNum = max(arr[p1], arr[p2])
            if arr[p1] > arr[p2]:
                #print("1")
                p2 += 1
            else:
                #print("2")
                p2 += 1
                p1 = p2 - 1

            if bestNum == maxNum:
                count += 1
                if count == k:
                    return maxNum
            else:
                count = 1
                if count == k:
                    return maxNum

            bestNum = maxNum
            
        