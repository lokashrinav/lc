class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        parent = {}

        for word in sentence1:
            parent[word] = word
        
        for word in sentence2:
            parent[word] = word

        for y, x in similarPairs:
            parent[y] = y
            parent[x] = x

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            first, second = find(a), find(b)
            
            if first == second:
                return
            
            parent[first] = second
        
        if len(sentence1) != len(sentence2):
            return False

        for y, x in similarPairs:
            union(y, x)
        
        for i in range(len(sentence1)):
            print(find(sentence1[i]), find(sentence2[i]))
            if find(sentence1[i]) != find(sentence2[i]):
                return False
        
        return True