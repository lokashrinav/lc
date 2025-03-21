class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = cows = 0
        secHmap = defaultdict(int)
        for i, elem in enumerate(secret):
            if elem == guess[i]:
                bulls += 1
            else:
                secHmap[elem] += 1
        
        for i, elem in enumerate(guess):
            if elem != secret[i]:
                if elem in secHmap and secHmap[elem] > 0:
                    cows += 1
                    secHmap[elem] -= 1
        
        return str(bulls) + "A" + str(cows) + "B"

                
        