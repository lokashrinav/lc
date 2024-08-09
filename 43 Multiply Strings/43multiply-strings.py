class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        multiply = 1
        for i in range(len(num2) - 1, -1, -1):
            sum1 = ""
            carry = 0
            #  738
            # sum = 0
            # sum = 8
            for p in range(len(num1) - 1, -1, -1):
                sum1 += str((int(num1[p]) * int(num2[i]) + carry) % 10)
                carry = ((int(num1[p]) * int(num2[i]) + carry) - ((int(num1[p]) * int(num2[i]) + carry) % 10)) // 10
                
                print("sum1", sum1)
                print("carry", carry)
                ''' 
                15 +
                '''

            if carry:
                sum1 = str(sum1) + str(carry)
            sum1 = int(sum1[::-1])
            print("sum", sum1)
            sum1 *= multiply
            multiply *= 10
            total += sum1            
        
        return str(total)

                

        