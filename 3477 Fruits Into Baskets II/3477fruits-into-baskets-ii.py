class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        # O(n^2)
        # O(n) - Memory
        
        total = 0
        for i in range(len(fruits)):
            flag = 1
            for p in range(len(baskets)):
                if fruits[i] <= baskets[p]:
                    baskets[p] *= -1
                    flag = 0
                    break

            total += flag
        
        return total
            





        