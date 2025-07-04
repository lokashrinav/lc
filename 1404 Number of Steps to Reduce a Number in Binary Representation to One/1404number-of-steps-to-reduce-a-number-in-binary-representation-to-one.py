class Solution:
    def numSteps(self, s: str) -> int:

        '''

        11001 -> 25

        25 -> 26 -> 13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1

        ''' 

        res = deque(list(s))
        total = 0
        carry = 0

        while len(res) > 1:
            if res[-1] == "1":
                res.pop()
                carry = 1
                for i in range(len(res) - 1, -1, -1):                      
                    if res[i] == "1" and carry:
                        res[i] = "0"
                    elif res[i] == "0" and carry:
                        res[i] = "1"
                        carry = 0
                        break
                    else:
                        break

                if carry:
                    res.appendleft("1")

                total += 2
            else:
                res.pop()
                total += 1
            print(res)
        
        return total



        