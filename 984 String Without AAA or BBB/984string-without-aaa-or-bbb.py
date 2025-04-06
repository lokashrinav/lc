class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        flag = False
        if a > b:
            flag = True
            a, b = b, a

        str1 = "c"
        while a or b:
            print(str1, a, b)
            if b > a * 2:
                if str1[-1] != 'b':
                    if b >= 2:
                        str1 += 'bb'
                        b -= 2
                    else:
                        str1 += 'b'
                        b -= 1
                else:
                    if a:
                        str1 += 'a'
                        a -= 1
            else:
                if str1[-1] != 'a':
                    # 13 b, 
                    # 5 a

                    if a >= 2 and (a - 2) * 2 >= b:
                        str1 += 'aa'
                        a -= 2
                    else:
                        str1 += 'a'
                        a -= 1
                else:
                    if b >= 2:
                        str1 += 'bb'
                        b -= 2
                    else:
                        str1 += 'b'
                        b -= 1

        if flag:
            new_str = ""
            for i in range(len(str1)):
                if str1[i] == 'b':
                    new_str += 'a'
                elif str1[i] == 'a':
                    new_str += 'b'
                else:
                    new_str += 'c'
            str1 = new_str

        return str1[1:]


