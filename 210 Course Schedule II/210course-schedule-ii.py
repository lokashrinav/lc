class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap2 = {}

        for list1 in prerequisites:
            if list1[0] not in hmap2.keys():
                hmap2[list1[0]] = []
            hmap2[list1[0]].append(list1[1])
        print(hmap2)
        cache = []
        visited = set()

        def dfs(num, curr):
            print(curr)
            if num in curr:
                return False
            if num in visited:
                return True
            if num not in hmap2.keys():
                visited.add(num)
                cache.append(num)
                return True
            visited.add(num)
            curr.add(num)
            for i in hmap2[num]:
                if(dfs(i, curr) == False):
                    return False
            curr.remove(num)
            cache.append(num)
            return True
            
        for i in range(numCourses):
            if i not in visited:
                curr = set()
                if(dfs(i, curr) == False):
                    return []

        return cache


        '''

        0 -> 1 -> 3
        0 -> 2 -> 3

        0 -> 1
          -> 2 -> 3

        '''
        