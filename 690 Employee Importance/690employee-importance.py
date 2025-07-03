"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        nodes = {}
        paths = defaultdict(list)

        for emp in employees:
            y, x, res = emp.id, emp.importance, emp.subordinates
            nodes[y] = x
            for elem in res:
                paths[y].append(elem)  
                
        cache = {}

        def dfs(elem):
            if elem in cache:
                return cache[elem]

            total = nodes[elem]
            for elem in paths[elem]:
                total += dfs(elem)
            cache[elem] = total
            return total

        '''
        for elem in nodes.keys():
            if elem not in cache:
                dfs(elem)

        print(nodes)'''
                
        return dfs(id)


        

            
        

        