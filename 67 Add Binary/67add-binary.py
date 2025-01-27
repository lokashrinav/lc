class Solution:
    def addBinary(self, a: str, b: str) -> str:

        p1 = len(a) - 1
        p2 = len(b) - 1
        
        new_str = []
        carry = 0
        while p1 >= 0 or p2  >= 0:
            if p1 >= 0 and p2 >= 0:
                total = (int(a[p1]) + int(b[p2]) + carry) % 2
                carry = (int(a[p1]) + int(b[p2]) + carry) // 2
            elif p1 >= 0:
                total = (int(a[p1]) + carry) % 2
                carry = (int(a[p1]) + carry) // 2
            elif p2 >= 0:
                total = (int(b[p2]) + carry) % 2
                carry = (int(b[p2]) + carry) // 2
            new_str.append(str(total))
            p1 -= 1
            p2 -= 1

        if carry:
            new_str.append("1")
        
        return ''.join(new_str[::-1])



        