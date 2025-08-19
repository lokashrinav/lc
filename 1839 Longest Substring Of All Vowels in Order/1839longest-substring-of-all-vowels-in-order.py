class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        maxLen = l = 0
        nex = {'a': ['a', 'e'], 'e': ['e', 'i'], 'i': ['i', 'o'], 'o': ['o', 'u'], 'u': ['u']}

        for i in range(len(word)):
            if l == i:
                if word[i] != 'a':
                    l += 1
            else:
                if word[i] not in nex[word[i - 1]]:
                    if word[i] != "a":
                        l = i + 1
                    else:
                        l = i
                if word[i] == 'u':
                    maxLen = max(i - l + 1, maxLen)

        return maxLen
            
