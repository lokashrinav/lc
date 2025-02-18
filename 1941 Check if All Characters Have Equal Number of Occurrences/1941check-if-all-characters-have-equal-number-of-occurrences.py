class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hmap = Counter(s)

        prev = None
        for key, val in hmap.items():
            if not prev:
                prev = val
            else:
                if prev != val:
                    return False
                prev = val
        
        return True