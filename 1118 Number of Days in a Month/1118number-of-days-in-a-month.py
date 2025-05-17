class Solution:
    def numberOfDays(self, year: int, month: int) -> int:

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 100 == 0 and year % 400 != 0):
            return days[month - 1]
        elif (year % 4) == 0:
            return days1[month - 1]
        else:
            return days[month - 1]
        