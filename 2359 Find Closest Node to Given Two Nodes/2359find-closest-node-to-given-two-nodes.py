class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        queue1 = deque([node1])
        queue2 = deque([node2])

        visited1 = set()
        visited2 = set()

        minInd = None

        while queue1 or queue2:
            print(queue1, queue2)
            minInd2 = None
            for i in range(len(queue1)):
                out = queue1.popleft()
                if out in visited1:
                    continue
                if out in visited2:
                    if minInd is None:
                        minInd = out
                    else:
                        minInd = min(out, minInd)
                if edges[out] != -1:
                    queue1.append(edges[out])
                visited1.add(out)

            for i in range(len(queue2)):
                out = queue2.popleft()
                if out in visited2:
                    continue

                if out in visited1:
                    if minInd is None:
                        minInd = out
                    else:
                        minInd = min(out, minInd)

                if edges[out] != -1 and edges[out] not in visited2:
                    queue2.append(edges[out])

                visited2.add(out)
            
            if minInd is not None:
                return minInd
        
        return -1



        
        