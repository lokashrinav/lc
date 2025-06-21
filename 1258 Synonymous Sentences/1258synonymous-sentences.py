class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        res = []
        text = text.split(" ")

        parent = {word: word for word in text}
        parent_list = {word: [word] for word in text}

        for y, x in synonyms:
            parent[y] = y
            parent[x] = x
            parent_list[y] = [y]
            parent_list[x] = [x]

        def union(a, b):
            first, second = find(a), find(b)

            if first == second:
                return 

            parent[second] = first
            parent_list[first] += parent_list[second]
            parent_list[first].sort()
            
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            
            return parent[a]

        for y, x in synonyms:
            union(y, x)
        
        print(parent_list)
                
        def dfs(i):
            if i == len(text):
                res.append(' '.join(text))
                return

            parent = find(text[i])

            for elem in parent_list[parent]:
                text[i] = elem
                dfs(i + 1)
        
        dfs(0)

        return res



        

