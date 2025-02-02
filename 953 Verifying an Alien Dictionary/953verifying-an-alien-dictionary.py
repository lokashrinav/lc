class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {}
        
        for i in range(len(order)):
            hmap[order[i]] = i

        def check(word1, word2):
            for i in range(min(len(word1),len(word2))):
                if hmap[word1[i]] < hmap[word2[i]]:
                    return True
                elif hmap[word1[i]] == hmap[word2[i]]:
                    continue
                else:
                    return False
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not check(words[i], words[i + 1]):
                return False
        
        return True
                
        