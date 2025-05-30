class Solution:
    def oddString(self, words: List[str]) -> str:

        def dint(word):
            diff = []
            for i in range(1, len(word)):
                diff.append(ord(word[i]) - ord(word[i - 1]))
            return tuple(diff)

        hmap = {}
        for i in range(len(words)):
            diff = dint(words[i])
            if diff in hmap:
                val, str1 = hmap[diff]
                hmap[diff] = (val + 1, words[i])
            else:
                hmap[diff] = (1, words[i])
        
        for key, val in hmap.items():
            if val[0] == 1:
                return val[1]
        

        