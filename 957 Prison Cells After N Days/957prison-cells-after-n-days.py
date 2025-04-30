class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        hset = set()
        res = []
        idk = 0
        for i in range(n):
            curr = [0] * 8

            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    curr[i] = 1

            cells = curr

            if tuple(cells) in hset:
                break

            hset.add(tuple(cells))
            res.append(cells)

        n -= 1
        print(res)
        if idk == n:
            print("1")
            return cells
        else:
            print("2")
            fun = n % len(res)
            print(fun)
            return res[fun]

