class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:

        if k >= len(bulbs):
            return -1            

        arr = [None] * len(bulbs)
        l, r = 0, len(bulbs) - 1
        saved = float('inf')

        while l <= r:
            arr = [None] * len(bulbs)
            queue = deque()
            m = (l + r) // 2

            for i in range(0, m + 1):
                arr[bulbs[i] - 1] = i
            
            for i in range(k + 1):
                if arr[i] is not None:
                    while queue and arr[i] <= queue[-1][0]:
                        queue.pop()
                    queue.append((arr[i], i))
                        
            flag = False

            #print(arr, m)

            for i in range(k + 1, len(bulbs)):
                #print(queue, arr[i - k - 1], arr[i])

                if queue and queue[0][1] + k + 1 <= i:
                    queue.popleft()
                
                
                if queue and (arr[i - k - 1] is not None and queue[0][0] > arr[i - k - 1]) and (arr[i] is not None and queue[0][0] > arr[i]):
                    flag = True
                elif not queue and arr[i] is not None and arr[i - k - 1] is not None:
                    saved = min(saved, m)
                    flag = True
                        
                if arr[i] is not None:
                    while queue and arr[i] <= queue[-1][0]:
                        queue.pop()
                    queue.append((arr[i], i))
            
            print(flag)
            
            if flag:
                r = m - 1
            else:
                l = m + 1
        
        if saved == float('inf'):
            return -1
    
        return saved + 1


            


        
