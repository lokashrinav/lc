class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        hmap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                final = word[:i] + '*' + word[i+1:]
                hmap[final].append(word)
        
        queue = deque([beginWord])
        level = 0
        visited = set()
        visited.add(beginWord)

        while queue:
            #print(queue)
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return level + 1

                for i in range(len(word)):
                    final = word[:i] + '*' + word[i+1:]
                    #print(final, hmap[final])
                    for word2 in hmap[final]:
                        if word2 not in visited:
                            queue.append(word2)
                            visited.add(word2)
                      

            level += 1
        
        return 0
        

