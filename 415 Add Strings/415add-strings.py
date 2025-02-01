class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1

        carry = 0
        total = 0

        new_str = []
        while p1 >= 0 or p2 >= 0 or carry:
            calc = (int(num1[p1]) if p1 >= 0 else 0) + (int(num2[p2]) if p2 >= 0 else 0) + carry
            if calc >= 10:
                curr = calc - 10
                carry = 1
            else:
                curr = calc
                carry = 0
            new_str.append(str(curr))
            p1 -= 1
            p2 -= 1

        return ''.join(new_str[::-1])




        