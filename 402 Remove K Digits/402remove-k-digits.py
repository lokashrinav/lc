class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''

        '''

        res = [float('inf')] * 10

        res2 = [float('inf')] * 10

        final = []

        for i in range(len(num) - 1, -1, -1):
            for p in range(int(num[i])):
                res[int(num[i])] = min(res[int(num[i])], res2[p])

            final.append(res[int(num[i])])

            res2[int(num[i])] = i

        final.reverse()
        queue = deque()

        for i in range(len(num)):
            if final[i] != float('inf') and final[i] - i <= k:
                k -= 1
            else:
                queue.append(num[i])

        while k:
            queue.pop()
            k -= 1
                
        while len(queue) > 1 and queue[0] == '0':
            queue.popleft()
        
        if not queue:
            return '0'
        
        return ''.join(queue)

        