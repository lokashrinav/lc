class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        recHmap = {}

        for i, elem in enumerate(recipes):
            recHmap[elem] = i

        supSet = set(supplies)

        def dfs(elem):
            if elem in visited:
                return visited[elem]
            if elem in supSet:
                visited[elem] = True
                return visited[elem]
            if elem in currVisited:
                visited[elem] = False
                return visited[elem]
            
            if elem not in recHmap:
                visited[elem] = False
                return visited[elem]
            
            currVisited.add(elem)

            for newElem in ingredients[recHmap[elem]]:
                val = dfs(newElem)
                if not val:
                    visited[elem] = False
                    return visited[elem]
            
            visited[elem] = True
            return visited[elem]
        
        res = []
        visited = {}
        for ind, elem in enumerate(recipes):
            currVisited = set()
            if elem not in visited:
                visited[elem] = dfs(elem)

            if visited[elem]:
                res.append(elem)

        return res

        