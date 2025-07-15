class Solution:
    def simplifyPath(self, path: str) -> str:

        elems = path.split("/")

        res = []
        for elem in elems:
            if elem:
                if elem == "..":
                    if len(res) >= 1:
                        res.pop()
                elif elem == ".":
                    continue
                else:
                    res.append(elem)
        
        str1 = "/" + '/'.join(res)

        return str1


        