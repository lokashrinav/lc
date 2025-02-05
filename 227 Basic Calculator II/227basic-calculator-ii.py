class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        prev_num, prev_op, total = 0, '+', 0
        s += '+'

        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            num = 0

            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            while i < len(s) and s[i] == ' ':
                i += 1
            
            op = s[i]

            if op in '+-/*':
                if prev_op == '+':
                    total += prev_num
                    prev_num = num
                elif prev_op == '-':
                    total += prev_num
                    prev_num = -num
                elif prev_op == '*':
                    prev_num *= num
                elif prev_op == '/':
                    prev_num = int(prev_num / num)
                
            prev_op = op
            i += 1
        
        return total + prev_num
                