class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        total = 0
        prev = 0
        total = 0
        flag = False

        for i in range(len(brackets)):
            back = brackets[i][0] - prev
            if brackets[i][0] >= income:
                back = income - prev
                flag = True

            total += (back) * (brackets[i][1] / 100)
            prev = brackets[i][0]

            print(total)

            if flag:
                break

        return total
        