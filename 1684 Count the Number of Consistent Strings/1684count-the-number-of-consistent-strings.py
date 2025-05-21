class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        hset = set(allowed)
        total = 0
        
        for word in words:
            count = 0
            for s in word:
                if s in hset:
                    count += 1
            if count == len(word):
                total += 1

        return total


        