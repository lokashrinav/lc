class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set = set(words)
        paths = defaultdict(list)
        paths[""] = []
        for i in range(len(words)):
            if words[i][:-1] in paths:
                paths[words[i][:-1]].append(words[i])
                paths[words[i]] = []
        
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