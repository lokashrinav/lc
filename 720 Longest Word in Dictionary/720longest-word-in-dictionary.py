class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        paths = defaultdict(list)
        for i in range(len(words)):
            for p in range(len(words)):
                if i == p:
                    continue
                if len(words[i]) + 1 == len(words[p]) and words[p][:-1] == words[i]:
                    paths[words[i]].append(words[p])
        
        maxNum = ""
        visited = set()
        
        def dfs(word):
            nonlocal maxNum
            if word in visited:
                return
            visited.add(word)
            if len(word) > len(maxNum):
                maxNum = word 
            elif len(word) == len(maxNum):
                maxNum = min(word, maxNum)

            for elem in paths[word]:
                dfs(elem)
        
        for i in range(len(words)):
            if len(words[i]) == 1:
                dfs(words[i])

        print(paths)

        return maxNum

