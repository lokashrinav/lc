class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        '''

        aabb

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] + 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + 1
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] + 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + 
        '''

        arr = [0] * 10
        new = arr.copy() 

        hmap = defaultdict(int)
        hmap[tuple(arr)] += 1
        total = 0
        for elem in word:
            arr[ord(elem) - 97] = ((arr[ord(elem) - 97] + 1) % 2)
            for i in range(10):
                if arr[i] == 1:
                    arr[i] = 0
                    total += hmap[tuple(arr)]
                    arr[i] = 1
                else:
                    arr[i] = 1
                    total += hmap[tuple(arr)]
                    arr[i] = 0
            total += hmap[tuple(arr)]
            hmap[tuple(arr)] += 1
        
        return total
