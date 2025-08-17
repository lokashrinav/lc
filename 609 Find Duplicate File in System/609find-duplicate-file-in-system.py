class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in range(len(paths)):
            s = paths[i].split(" ")
            for i in range(1, len(s)):
                new = s[i].split("(")
                content = new[-1][:-1]
                hmap[content].append(s[0] + "/" + new[0])
                
        return [val for key, val in hmap.items() if len(val) >= 2]

        