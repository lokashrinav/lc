class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        '''
        a subsequence that maximizes scores
        '''

        hmap = Counter(letters)
        cache = {}

        def dfs(ind):
            print(ind, hmap)

            if ind == len(words):
                return 0
            
            if (ind, frozenset(sorted(hmap.items()))) in cache:
                return cache[(ind, frozenset(sorted(hmap.items())))]

            maxNum = dfs(ind + 1)

            flag = True
            scotty = 0
            for elem in words[ind]:
                hmap[elem] -= 1
                scotty += score[ord(elem) - 97]
                if hmap[elem] < 0:
                    flag = False
            
            if flag:
                maxNum = max(maxNum, scotty + dfs(ind + 1))

            for elem in words[ind]:
                hmap[elem] += 1
            
            cache[(ind, frozenset(sorted(hmap.items())))] = maxNum

            return maxNum
            
        return dfs(0)