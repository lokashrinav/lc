class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        i = 0

        while i < len(expression):
            sign = 1

            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            
            numer = 0

            while i < len(expression) and expression[i].isdigit():
                numer = 10 * numer + int(expression[i])
                i += 1
            
            i += 1

            denom = 0
            while i < len(expression) and expression[i].isdigit():
                denom = 10 * denom + int(expression[i])
                i += 1

            num = num * denom + sign * numer * den
            den *= denom

            gcd = math.gcd(num, den)
            num //= gcd
            den //= gcd
            
        return str(num) + "/" + str(den)