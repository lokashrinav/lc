class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        count = 0
        
        for elem1 in a:
            for elem2 in b:
                for elem3 in c:
                    if (elem1 ^ elem2 ^ elem3).bit_count() % 2 == 0:
                        count += 1

        return count
        


        