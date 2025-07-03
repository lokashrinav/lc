class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reservedSeats.sort()

        total = n * 2

        hmap = defaultdict(list)

        for y, x in reservedSeats:
            hmap[y].append(x)
        
        for y in hmap.keys():
            print(y, total)
            flag = False
            for elem in [2, 3, 4, 5, 6, 7, 8, 9]:
                if elem in hmap[y]:
                    flag = True
                    break
            
            if not flag:
                continue
            
            flag = False
            for elem in [4, 5, 6, 7]:
                if elem in hmap[y]:
                    flag = True
                    break
            
            if not flag:
                total -= 1
                continue

            flag = False
            for elem in [2, 3, 4, 5]:
                if elem in hmap[y]:
                    flag = True
                    break

            if not flag:
                total -= 1
                continue
            
            flag = False
            for elem in [6, 7, 8, 9]:
                if elem in hmap[y]:
                    flag = True
                    break

            if not flag:
                total -= 1
                continue
            
            total -= 2
            
        
        return total
        


        

        