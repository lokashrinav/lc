class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for i in range(len(columnTitle)):
            num += ord(columnTitle[i]) - 65 + 1
            print(num)
            num *= 26
        return int(num / 26)

        