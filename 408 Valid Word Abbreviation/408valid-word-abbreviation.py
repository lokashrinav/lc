class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2].isdigit():
                if abbr[p2] == "0": return False
                num = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    num = num * 10 + int(abbr[p2])
                    p2 += 1
                p1 += num
            else:
                if word[p1] == abbr[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
        
        return len(word) == p1 and len(abbr) == p2