class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def build_graph(words):
            graph = defaultdict(set)
            
            for i in range(len(words) - 1):
                word1, word2 = words[i], words[i + 1]
                
                # Find first different character
                for j in range(min(len(word1), len(word2))):
                    if word1[j] != word2[j]:
                        # word1[j] comes before word2[j]
                        graph[word1[j]].add(word2[j])
                        break  # Only need first difference
                else:
                    # word1 is prefix of word2, check if valid
                    if len(word1) > len(word2):
                        return None  # Invalid: "abc" before "ab"
            
            return graph
        
        graph = build_graph(words)
        
        if graph is None:  # ADD THIS CHECK
            return ""

        queue = deque()
        result = []
        all_chars = set(''.join(words))

        in_degree = {char: 0 for char in all_chars}
        for node in graph:
            for nei in graph[node]:
                in_degree[nei] += 1
        
        # FIXED: Check ALL characters for 0 in-degree
        queue = deque([char for char in all_chars if in_degree[char] == 0])
        result = []

        while queue:
            out = queue.popleft()
            result.append(out)

            for node in graph[out]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
        
        return ''.join(result) if len(result) == len(all_chars) else ""
