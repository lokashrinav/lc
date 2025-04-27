class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        self.parent = [i for i in range(n)]
        answers = []

        def find(a):
            if self.parent[a] != a:
                self.parent[a] = find(self.parent[a])

            return self.parent[a]

        def union(a, b):
            p_a, p_b = find(a), find(b)
            if p_a == p_b:
                return

            self.parent[p_a] = p_b

        for i in range(1, len(nums)):
            if abs(nums[i - 1] - nums[i]) <= maxDiff:
                union(i - 1, i)

        for y, x in queries:
            answers.append(find(y) == find(x))

        return answers
                

        

            