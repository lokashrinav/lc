class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        hmap = {}
        for i in range(len(answers)):
            if answers[i] in hmap:
                hmap[answers[i]] -= 1
                if hmap[answers[i]] == 0:
                    del hmap[answers[i]]
            else:
                if answers[i] > 0:
                    hmap[answers[i]] = answers[i]
        
        for key, val in hmap.items():
            print(key, val)
        
        return sum(hmap.values()) + len(answers)
        
