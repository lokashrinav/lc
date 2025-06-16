class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prev = 0
        total = 0
        for i in range(len(bank)):
            if bank[i].count("1"):
                total += prev * bank[i].count("1")
                prev = bank[i].count("1")
        
        return total
        