class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        vowels = ['a', 'e', 'i', 'o', 'u']

        hmap1 = {}
        hmap2 = {}
        hmap = {}
        for i in range(len(wordlist)):
            word = list(wordlist[i])
            if wordlist[i] not in hmap2:
                hmap2[wordlist[i]] = i
            if wordlist[i].lower() not in hmap1:
                hmap1[wordlist[i].lower()] = i
            for p in range(len(word)):
                if word[p].lower() in vowels:
                    word[p] = '?'
                else:
                    word[p] = word[p].lower()
            w = ''.join(word)
            if w not in hmap:
                hmap[w] = i
        
        for query in queries:
            word = list(query)
            if query in hmap2:
                res.append(wordlist[hmap2[query]])
                continue
            elif query.lower() in hmap1:
                res.append(wordlist[hmap1[query.lower()]])
                continue
            for p in range(len(word)):
                if word[p].lower() in vowels:
                    word[p] = '?'
                else:
                    word[p] = word[p].lower()
                    
            if ''.join(word) in hmap:
                res.append(wordlist[hmap[''.join(word)]])
            else:
                res.append("")
        
        return res


        
            
        