class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        hmap = {}
        for i in range(len(cpdomains)):
            curr = cpdomains[i]
            numVisits, domain = curr.split(" ")
            idk = domain.split(".")
            currStr = idk[-1]
            for i in range(len(idk) - 2, -2, -1):
                if currStr in hmap:
                    hmap[currStr] += int(numVisits)
                else:
                    hmap[currStr] = int(numVisits)
                currStr = idk[i] + "." + currStr

        for key in hmap.keys():
            res.append(str(hmap[key]) + " " + str(key))   

        return res

        

        