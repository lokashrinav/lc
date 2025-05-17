class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        s = list(s)

        paths = defaultdict(list)

        # alph = [0] * 26

        list2 = []

        for i in range(len(pairs)):
            paths[pairs[i][0]].append(pairs[i][1])
            paths[pairs[i][1]].append(pairs[i][0])
        
        visited = set()

        def dfs(num):
            if num in visited:
                return

            list1.append(num)
            list2.append(s[num])
            visited.add(num)
            for elem in paths[num]:
                dfs(elem)

        for i in range(len(s)):
            alph = [0] * 26
            list1 = []
            list2 = []
            if i in visited:
                continue

            dfs(i)

            list1.sort()
            list2.sort()

            for i in range(len(list1)):
                s[list1[i]] = list2[i]
        
        return ''.join(s)



        


