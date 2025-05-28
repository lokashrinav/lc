class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        bestHand = "High Card"
        hmap = Counter(ranks)

        if max(hmap.values()) == 2:
            bestHand = "Pair"
        
        if max(hmap.values()) >= 3:
            bestHand = "Three of a Kind"

        if len(set(suits)) == 1:
            bestHand = "Flush"
        
        return bestHand