class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        stack = []
        while i < len(path):
            while i < len(path) and path[i] == '/':
                i += 1
            
            str1 = ""
            while i < len(path) and path[i] != '/':
                str1 += path[i]
                i += 1

            if str1 == ".":
                continue
            elif str1 == "..":
                if stack:
                    stack.pop()
            else:
                if str1:
                    stack.append(str1)
            
            i += 1
        return '/' + '/'.join(stack)

                
            


        