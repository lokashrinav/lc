class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        Cannot contain alphabet unless e

        no op symbols in a row

        integer followed by sign

        needs to contain a number

        op can't be after number
        '''

        if not s:
            return False

        alph = [chr(i) for i in range(97, 123)]

        alph2 = [chr(i) for i in range(65, 91)]

        alph += alph2

        nums = [i for i in range(1, 10)]
        flag = False

        for elem in s:
            if elem.isdigit():
                flag = True
            if elem in alph and (elem != 'e' and elem != 'E'):
                return False

        if not flag:
            return False

        
        flag = False
        for i in range(len(s)):
            if not flag and s[i] in 'eE':
                return False
            elif s[i].isdigit():
                flag = True

        flag = False
        for i in range(len(s)):
            if flag and (s[i] == '-' or s[i] == '+'):
                if i - 1 >= 0 and (s[i - 1] == 'e' or s[i - 1] == "E") and i + 1 < len(s) and s[i + 1].isdigit():
                    continue

                return False

            if s[i].isdigit():
                flag = True
                
        for i in range(1, len(s)):
            if (s[i - 1] == '-' or s[i - 1] == '+') and (s[i] == '-' or s[i] == '+'):
                return False
        
        
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if i - 1 >= 0 and (s[i - 1].isdigit() or (i - 2 >= 0 and s[i - 1] == '.' and s[i - 2].isdigit)) and i + 1 < len(s) and (s[i + 1].isdigit() or s[i + 1] == '+' or s[i + 1] == '-'):
                    continue
                else:
                    return False
        
        # if there exists a digit after an 
        # two bullet points in a row
        # bullet point at the end

        for i in range(1, len(s)):
            if s[i - 1] == '.' and s[i] == '.':
                return False
                
        flag = False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                flag = True
            elif s[i] == '.' and flag:
                return False

        if s.count('.') >= 2 or s.count('e') >= 2:
            return False    


        flag = False
        for i in range(len(s)):
            if flag and s[i] in '-+':
                return False
            elif s[i] == '.':
                flag = True
            elif s[i] == 'e':
                flag = False

                  
        return True
        


        
        
        