class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        buckets = defaultdict(lambda: defaultdict(int))
        ans = 0
        for i, v in enumerate(nums):
            g = math.gcd(i, k)
            for h, c in buckets[v].items():
                if (g * h) % k == 0:
                    ans += c
            buckets[v][g] += 1
        return ans
        



        


        