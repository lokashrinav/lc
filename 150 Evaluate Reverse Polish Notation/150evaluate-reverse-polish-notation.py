class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in range(len(tokens)):
            if tokens[i] in '+*-/':
                first = stack.pop()
                second = stack.pop()
                if tokens[i] == '+':
                    stack.append(str(int(first) + int(second)))
                elif tokens[i] == '*':
                    stack.append(str(int(first) * int(second)))
                elif tokens[i] == '/':
                    div = int(second) / int(first)
                    stack.append(str(int(div)))
                else:
                    stack.append(str(int(second) - int(first)))
            else:
                stack.append(tokens[i])
            # print(stack)
        return int(stack[0])