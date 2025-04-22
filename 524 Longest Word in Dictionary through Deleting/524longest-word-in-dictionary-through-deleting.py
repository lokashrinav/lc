class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        sol = ""

        for string in dictionary:
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(string):
                if s[p1] == string[p2]:
                    p1 += 1
                    p2 += 1
                elif s[p1] != string[p2]:
                    p1 += 1

            if p2 == len(string):
                if len(string) > len(sol):
                    sol = string
                elif len(string) == len(sol):
                    if string < sol:
                        sol = string
        

        return sol