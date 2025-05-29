class Solution:
    def countValidWords(self, sentence: str) -> int:

        def func(a):

            if a.count("-") >= 2 or a.count(".") >= 2 or a.count(",") >= 2 or a.count("!") >= 2:
                return False

            for i in range(len(a)):
                if a[i].isdigit():
                    return False
                elif a[i] == '-':
                    if i - 1 >= 0 and i + 1 < len(a):
                        if a[i - 1].isalpha() and a[i + 1].isalpha():
                            continue
                    return False
                elif a[i] == '.' or a[i] == ',' or a[i] == '!':
                    if i == len(a) - 1:
                        continue

                    return False
            
            return True
                

        s = sentence.split(" ")

        count = 0
        for elem in s:
            if elem:
                if func(elem):
                    count += 1
        
        return count
        