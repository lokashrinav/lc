class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        '''




        '''

        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix = [0]
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        res = []
        for y, x in queries:
            res.append(prefix[x + 1] - prefix[y])
        
        return res

        