class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        lis = date.split("-")
        total = 0
        for i in range(int(lis[1])):
            if i == 2 and ((int(lis[0]) % 4 == 0 and int(lis[0]) % 100 != 0) or int(lis[0]) % 400 == 0):
                total += 29
            else:
                total += days[i]

        return total + int(lis[-1])

        