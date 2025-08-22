class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        res = []
        alph = set()
        for i in range(len(phrases)):
            for p in range(len(phrases)):
                if i == p:
                    continue
                first = phrases[i].split(" ")
                second = phrases[p].split(" ")

                if first[-1] == second[0]:
                    new1 = ' '.join(first[:-1])
                    new2 = ' '.join(second)
                    mid = ' ' if new1 and new2 else ''
                    alph.add(new1 + mid + new2)
        
        alph = list(alph)
        alph.sort()

        return alph

                

        