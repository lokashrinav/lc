class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        res = []
        
        def dfs(ind, comma, curr):
            if ind >= len(s):
                if not comma:
                    return
                idk = curr.split(", ")
                print(idk)
                num1 = idk[0][1:]
                num2 = idk[1][:-1]
                
                if num1.count(".") > 1 or num2.count(".") > 1:
                    return 
                
                if not num1 or not num2:
                    return

                if num1[-1] in " ,." or num2[-1] in " ,.":
                    return 

                if (num1.count(".") == 1 and num1[-1] == "0") or (num2.count(".") == 1 and num2[-1] == "0"):
                    return
                
                if (len(num1) >= 2 and num1[0] == "0" and num1[1] != ".") or (len(num2) >= 2 and num2[0] == "0" and num2[1] != "."):
                    return
                
                res.append(curr)

                return

            if s[ind] in "()":
                dfs(ind + 1, comma, curr + s[ind])
                return
            
            if not comma:
                dfs(ind + 1, True, curr + s[ind] + ", ")

            dfs(ind + 1, comma, curr + s[ind])

            dfs(ind + 1, comma, curr + s[ind] + ".")

        dfs(0, False, "")

        return res