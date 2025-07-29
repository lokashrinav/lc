class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []

        paths = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                for p in range(26):
                    if chr(p + 97) != word[i]:
                        paths[word[:i] + chr(p + 97) + word[i+1:]].append(word)
        
        #print(paths)

        parents = defaultdict(set)
        queue = deque([beginWord])
        visited = set()
        count = 0
        length = None
        while queue:
            flag = False
            current_level_nodes = set()
            for i in range(len(queue)):
                out = queue.popleft()
                if out == endWord:
                    flag = True
                    length = count
                    continue

                for elem in paths[out]:
                    if elem not in visited:  # Only unvisited nodes
                        parents[elem].add(out)  # Multiple words can reach same neighbor
                        current_level_nodes.add(elem)

            for node in current_level_nodes:
                queue.append(node)
            
            count += 1
            visited.update(current_level_nodes)

            if flag:
                break
        
        #print("HI")
        new = {}
        res = []

        def backtrack(word, length):
            #print(word, length)
            if word == beginWord:
                return [[beginWord]]
            if length == 0:
                return []

            curr = []
            for elem in parents[word]:
                calc = backtrack(elem, length - 1)
                for elem in calc:
                    curr.append([word] + elem)
            
            return curr
        
        if length is None:
            return []

        returned = backtrack(endWord, length)

        for i in range(len(returned)):
            returned[i] = returned[i][::-1]
                
        return list(set(tuple(ret) for ret in returned))