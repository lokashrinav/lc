class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hmap = Counter(words1)

        count = 0
        hmap2 = hmap.copy()

        for word in words2:
            if word in hmap2:
                hmap2[word] += 1
        
        for word in words2:
            if hmap[word] == 1 and hmap2[word] == 2:
                count += 1

        return count
