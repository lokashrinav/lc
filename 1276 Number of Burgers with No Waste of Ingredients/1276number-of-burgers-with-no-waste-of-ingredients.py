class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:

        if cheeseSlices * 2 <= tomatoSlices <= cheeseSlices * 4 and tomatoSlices % 2 == 0:
            fun = tomatoSlices - cheeseSlices * 2
            return [fun // 2, cheeseSlices - fun // 2]
        
        return []

        