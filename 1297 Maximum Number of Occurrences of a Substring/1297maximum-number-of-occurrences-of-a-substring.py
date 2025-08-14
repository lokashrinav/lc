class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        hmap = defaultdict(int)
        for i in range(minSize, maxSize + 1):
            count = 0
            arr = [0] * 26
            for p in range(i):
                if arr[ord(s[p]) - 97] == 0:
                    count += 1
                arr[ord(s[p]) - 97] += 1
            
            #print(count)
            
            if count <= maxLetters:
                hmap[s[:i]] += 1
                        
            for p in range(len(s) - i):
                arr[ord(s[p]) - 97] -= 1
                if arr[ord(s[p]) - 97] == 0:
                    count -= 1
                if arr[ord(s[p + i]) - 97] == 0:
                    count += 1
                arr[ord(s[p + i]) - 97] += 1
                if count <= maxLetters:
                    hmap[s[p+1:p+i+1]] += 1
            
            #print(hmap)

        if not hmap:
            return 0

        return max(hmap.values())