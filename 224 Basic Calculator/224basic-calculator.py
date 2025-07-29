class Solution:
    def calculate(self, s: str) -> int:

        s = s.replace('+', ' + ')
        s = s.replace('(', ' ( ')
        s = s.replace(')', ' ) ')
        s = s.replace('-', ' - ')

        s = s.split(" ")
        res = []

        for elem in s:
            if elem:
                res.append(elem)

        print(res)

        def dfs(ind):
            if ind == len(res):
                return (ind, 0)
            
            stack = []
            curr = 0
            while ind < len(res):
                if res[ind] == "(":
                    ind, ret = dfs(ind + 1)
                    if not stack:
                        curr += ret
                    elif stack[-1] == "+":
                        stack.pop()
                        curr += ret
                    else:
                        stack.pop()
                        curr -= ret
                elif res[ind] == ")":
                    return (ind + 1, curr)
                elif res[ind] == "-":
                    stack.append("-")
                    ind += 1
                elif res[ind] == "+":
                    stack.append("+")
                    ind += 1
                else:
                    if not stack:
                        curr += int(res[ind])
                    elif stack[-1] == "+":
                        stack.pop()
                        curr += int(res[ind])
                    else:
                        stack.pop()
                        curr -= int(res[ind])

                    ind += 1
                
            return (ind, curr)
            
        calc = dfs(0)

        return calc[1]


        