class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        hmap = {}
        arr = []
        for name in names:
            if name not in hmap:
                hmap[name] = 1
                arr.append(name)
            else:
                k = hmap[name]
                newName = name + "(" + str(k) + ")"
                while newName in hmap:
                    k += 1
                    newName = name + "(" + str(k) + ")"
                hmap[name] += 1
                hmap[newName] = 1
                arr.append(newName)
        
        return arr