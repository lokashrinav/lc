class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        first = words[::]

        pat = list(pattern)
        hmap = {}
        prev = 'a'
        for i, elem in enumerate(pat):
            if elem not in hmap:
                hmap[elem] = prev
                prev = chr(ord(prev) + 1)

            pat[i] = hmap[elem]
        
        for i in range(len(words)):
            words[i] = list(words[i])

        for word in words:
            hmap = {}      
            prev = 'a'
            for i, elem in enumerate(word):
                if elem not in hmap:
                    hmap[elem] = prev
                    prev = chr(ord(prev) + 1)
                word[i] = hmap[elem]
        
        final = []
        for i in range(len(words)):
            if words[i] == pat:
                final.append(first[i])
            
        return final

        
        