class Solution:
    def minMaxDifference(self, num: int) -> int:

        saved = None
        num_list = list(str(num))

        for i in range(len(str(num))):
            if num_list[i] != "9":
                saved = num_list[i]
                break
        
        for i in range(len(str(num))):
            if num_list[i] == saved:
                num_list[i] = "9"
        
        num1 = int(''.join(num_list))

        num_list = list(str(num))
        saved = None
        for i in range(len(str(num))):
            if num_list[i] != "0":
                saved = num_list[i]
                break
        
        for i in range(len(str(num))):
            if num_list[i] == saved:
                num_list[i] = "0"
        
        num2 = int(''.join(num_list))

        return num1 - num2
                

            

        