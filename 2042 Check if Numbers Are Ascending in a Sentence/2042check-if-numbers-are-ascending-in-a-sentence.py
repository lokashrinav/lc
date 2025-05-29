class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        res = s.split(" ")

        print(res)

        prev = -1

        for elem in res:
            if elem.isdigit() and int(elem) > prev:
                prev = int(elem)
            elif elem.isdigit():
                return False
        
        return True
