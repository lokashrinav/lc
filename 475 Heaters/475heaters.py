class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()

        def func(m):
            res = []
            for heater in heaters:
                res.append([heater - m, heater + m])
            
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if res[j][1] >= houses[i] >= res[j][0]:
                    i += 1
                else:
                    j += 1
            
            return i == len(houses)


        
        l, r = 0, max(max(heaters), max(houses))

        while l < r:
            m = (l + r) // 2
            if func(m):
                r = m
            else:
                l = m + 1
        
        return l
            
