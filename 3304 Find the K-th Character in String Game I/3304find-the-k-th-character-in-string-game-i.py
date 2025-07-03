class Solution:
    def kthCharacter(self, k: int) -> str:

        res = ["a"]
        
        while len(res) < k:
            for p in range(len(res)):
                res.append(chr((ord(res[p]) - 96) % 26 + 97))
        
        print(res)
        
        return res[k - 1]

        