class Solution:
    def interpret(self, command: str) -> str:

        i = 0 
        str1 = ""
        while i < len(command):
            if command[i] == "G":
                str1 += "G"
                i += 1
            elif command[i:i+2] == "()":
                str1 += "o"
                i += 2
            else:
                str1 += "al"
                i += 4
        
        return str1

        