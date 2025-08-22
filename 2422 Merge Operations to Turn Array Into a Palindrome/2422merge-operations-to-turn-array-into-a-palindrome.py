class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        '''

        4, 3, 2, 3, 4

        '''

        queue = deque(nums)
        total = 0

        while len(queue) >= 2:
            if queue[0] == queue[-1]:
                queue.pop()
                if queue:
                    queue.popleft()
            elif queue[0] > queue[-1]:
                out1 = queue.pop()
                out2 = queue.pop()
                queue.append(out1 + out2)
                total += 1
            else:
                out1 = queue.popleft()
                out2 = queue.popleft()
                queue.appendleft(out1 + out2) 
                total += 1
                
        return total
        


        