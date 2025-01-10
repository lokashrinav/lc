class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = []
        prevHmap = {}
        for i in range(len(words2)):
            hmap = {}
            for word in words2[i]:
                hmap[word] = hmap.get(word, 0) + 1
            
            for key, val in hmap.items():
                if key not in prevHmap:
                    prevHmap[key] = val
                else:
                    prevHmap[key] = max(val, prevHmap[key])

        
        for p in range(len(words1)):
            changed = True
            hmap = {}
            for word in words1[p]:
                hmap[word] = hmap.get(word, 0) + 1

            for key, val in prevHmap.items():
                if key in hmap:
                    if hmap[key] < prevHmap[key]:
                        changed = False
                        break
                else:
                    changed = False
                    break

            if changed:
                res.append(words1[p])

        return res

