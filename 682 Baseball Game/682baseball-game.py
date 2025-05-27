class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []
        start = None
        for i in range(len(operations)):
            op = operations[i]
            if op.isdigit() or op[1:].isdigit():
                print(op, int(op))
                res.append(int(op))
            elif op == "+":
                res.append(res[-1] + res[-2])
            elif op == "C":
                res.pop()
            else:
                res.append(res[-1] * 2)
            print(res)
        
        return sum(res)


        