class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hmap = Counter(digits)
        res = []

        for i in range(100, 1000, 2):
            flag = True
            for elem in str(i):
                if not (int(elem) in hmap and hmap[int(elem)] > 0):
                    flag = False
                if int(elem) in hmap:
                    hmap[int(elem)] -= 1

            for elem in str(i):
                if int(elem) in hmap:
                    hmap[int(elem)] += 1

            if flag:
                res.append(i)
        
        return res

                