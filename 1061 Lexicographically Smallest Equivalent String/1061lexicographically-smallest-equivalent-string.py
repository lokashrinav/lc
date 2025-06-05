class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        paths = defaultdict(list)
        for i in range(len(s1)):
            paths[s1[i]].append(s2[i])
            paths[s2[i]].append(s1[i])

        def dfs(char):
            if char in visited:
                return visited[char]
            
            if char in curr:
                return None

            curr.add(char)

            minChar = char
            for elem in paths[char]:
                calc = dfs(elem)
                if calc:
                    minChar = min(calc, minChar)

            return minChar

        baseStr = list(baseStr)
        visited = {}

        for i in range(len(baseStr)):
            curr = set()
            baseStr[i] = dfs(baseStr[i])
            for elem in curr:
                visited[elem] = baseStr[i]
        
        return ''.join(baseStr)
        