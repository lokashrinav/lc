class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        first_num1, second_num1 = num1.split("+")
        first_num2, second_num2 = num2.split("+")

        
        first = int(first_num1) * int(first_num2)
        second = -1 * int(second_num1[:-1]) * int(second_num2[:-1])

        new_first = first + second
        new_second = int(first_num1) * int(second_num2[:-1]) + int(first_num2) * int(second_num1[:-1])

        return str(new_first) + '+' + str(new_second) + 'i'


