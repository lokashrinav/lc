class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hmapHand = Counter(hand)
        heap = []
        for elem in hmapHand:
            heapq.heappush(heap, elem)

        count = 0
        smallest = None
        for i in range(len(hand)):
            if count == groupSize:
                count = 0
            if count == 0:
                if heap[0] in hmapHand:
                    hmapHand[heap[0]] -= 1
                    if hmapHand[heap[0]] == 0:
                        smallest = heapq.heappop(heap)
                    else:
                        smallest = heap[0]
                else:
                    return False
                count += 1
            else:
                if smallest + 1 in hmapHand:
                    hmapHand[smallest + 1] -= 1
                    if hmapHand[smallest + 1] == 0 and smallest + 1 == heap[0]:
                        heapq.heappop(heap)
                        smallest += 1
                    elif hmapHand[smallest + 1] != 0:
                        smallest += 1
                    else:
                        return False    
                else:
                    return False
                count += 1        
        return True
        