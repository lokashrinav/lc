class Solution:
    def differByOne(self, dict1: List[str]) -> bool:
        if not dict1:
            return False
        
        L = len(dict1[0])
        # for each position i, see if removing that char
        # makes two words collide
        for i in range(L):
            seen = set()
            for w in dict1:
                # drop character at i
                pattern = w[:i] + w[i+1:]
                if pattern in seen:
                    return True
                seen.add(pattern)
            # once we've checked all words at index i,
            # we can discard 'seen' and move on
        
        return False
