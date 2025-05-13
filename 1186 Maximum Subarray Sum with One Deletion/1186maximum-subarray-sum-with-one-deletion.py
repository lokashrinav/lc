class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        flag = False
        for elem in arr:
            if elem > 0:
                flag = True
        
        if not flag:
            return max(arr)

        # def dfs(ind):
                    
        
        curr = 0
        maxNum = 0
        res = []
        fin = []

        for i in range(len(arr)):
            prev = curr
            curr += arr[i]
            if arr[i] < 0:
                fin.append((prev, i))
            if curr < 0:
                curr = 0
                fin.append((prev, i))
            maxNum = max(maxNum, curr)
        
        curr2 = 0
        maxNum2 = 0
        idk = []

        for i in range(len(arr) - 1, -1, -1):
            prev = curr2
            curr2 += arr[i]
            if curr2 < 0:
                curr2 = 0
            maxNum2 = max(maxNum2, curr2)
            idk.append(curr2)
        
        idk.reverse()

        idk.append(0)
        print(fin)
        print(idk)

        for y, x in fin:
            maxNum = max(y + idk[x + 1], maxNum)

        return maxNum
                


        