class Solution:
    def reverse(self, x: int) -> int:
        carry = ""
        if x < 0:
            carry = "-"
            x = str(x)[1:]
        else:
            x = str(x)

        if len(str(x)) > len(str(2 ** 31)):
            return 0
        
        if len(str(x)) < len(str(2 ** 31)):
            return int(str(x)[::-1]) if not carry else -int(str(x)[::-1])

        if not carry:
            x = str(x)[::-1]
            print(x)
            print(2 ** 31 - 1)
            i = 0
            while i < len(str(2 ** 31 - 1)):
                if int(x[i]) < int(str(2 ** 31 - 1)[i]):
                    break
                if int(x[i]) > int(str(2 ** 31 - 1)[i]):
                    return 0
                i += 1
        else:
            x = str(x)[::-1]
            i = 0
            while i < len(str(2 ** 31)):
                if int(x[i]) < int(str(2 ** 31)[i]):
                    break
                if int(x[i]) > int(str(2 ** 31)[i]):
                    return 0
                i += 1

        return int(str(x)) if not carry else -int(str(x))

        