class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        hmap = defaultdict(int)
        for i in range(min(k, len(s))):
            if s[i] in vowels:
                hmap[s[i]] += 1

        maxNum = sum(hmap.values())

        for i in range(k, len(s)):
            if s[i] in vowels:
                hmap[s[i]] += 1
            if s[i - k] in vowels:
                hmap[s[i - k]] -= 1

            maxNum = max(maxNum, sum(hmap.values()))
        
        return maxNum


