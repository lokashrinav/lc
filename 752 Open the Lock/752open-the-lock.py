class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        hset = set(deadends)

        queue = deque(['0000'])
        count = 0
        visited = set()

        while queue:
            for i in range(len(queue)):
                out = queue.popleft()

                if out == target:
                    return count

                if out in visited or out in hset:
                    continue
                
                visited.add(out)

                for i in range(4):
                    queue.append(out[:i] + str((int(out[i]) - 1 + 10) % 10) + out[i+1:])
                    queue.append(out[:i] + str((int(out[i]) + 1) % 10) + out[i+1:])

            count += 1
        
        return -1
