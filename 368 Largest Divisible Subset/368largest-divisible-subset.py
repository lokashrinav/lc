class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''

        answer[i] % answer[j] == 0 - if i first, True, else False
        answer[j] % answer[i] == 0 - 

        3, 18, 12, 2, 6

        18 -> 6, 3, 2
        12 -> 6, 3, 2   
        '''

        paths = defaultdict(list)
        for i in range(len(nums)):
            for p in range(i - 1, -1, -1):
                if nums[i] % nums[p] == 0:
                    paths[nums[i]].append(nums[p])
                elif nums[p] % nums[i] == 0:                
                    paths[nums[p]].append(nums[i])

        visited = {}

        def dfs(num):
            if num in visited:
                return visited[num]
                
            maxNum = 0
            saved = []

            for elem in paths[num]:
                calc = dfs(elem)
                if calc[0] > maxNum:
                    maxNum = calc[0]
                    saved = calc[1].copy()

            saved.append(num)

            visited[num] = (1 + maxNum, saved.copy())

            return visited[num]  
                  
        maxNum = 0
        saved = []
        for i in range(len(nums)):
            calc = dfs(nums[i])
            if calc[0] > maxNum:
                maxNum = calc[0]
                saved = calc[1]
        
        print(paths, visited)
        print(maxNum, saved)

        return saved
