class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        count = 0

        hmap = [[None] * 26 for i in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            if i + 1 < len(s):
                hmap[i] = hmap[i + 1].copy()
            hmap[i][ord(s[i]) - 97] = i

        def check(word):
            if len(word) > len(s):
                return False

            if not word:
                return True

            p1 = 0
            for i in range(len(word)):
                prev = p1
                if p1 >= len(s):
                    return False

                p1 = hmap[p1][ord(word[i]) - 97]
                if p1 is None:
                    return False
                p1 += 1
                    

            return True

        p1 = p2 = 0
        total = 0

        for word in words:
            if check(word):
                total += 1
        
        return total

                
