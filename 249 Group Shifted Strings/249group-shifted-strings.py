class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)

        for i in range(len(strings)):
            length = len(strings[i])
            diff = []
            for p in range(len(strings[i]) - 1):
                calc = (ord(strings[i][p]) - ord(strings[i][p + 1])) % 26
                diff.append(calc)
            hmap[(length, tuple(diff))].append(strings[i])
        
        return list(hmap.values())