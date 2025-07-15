class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token == "+":
                out1 = stack.pop()
                out2 = stack.pop()
                stack.append(out1 + out2)
            elif token == "-":
                out1 = stack.pop()
                out2 = stack.pop()
                stack.append(out2 - out1)
            elif token == "*":
                out1 = stack.pop()
                out2 = stack.pop()
                stack.append(out1 * out2)
            elif token == '/':
                out1 = stack.pop()
                out2 = stack.pop()
                stack.append(int(out2 / out1))
            else:
                stack.append(int(token))

        return stack[0]