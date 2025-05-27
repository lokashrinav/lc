class Solution:
    def reformat(self, s: str) -> str:

        digits = []
        letters = []
        for elem in s:
            if elem.isdigit():
                digits.append(elem)
            else:
                letters.append(elem)
        
        final = []
        while digits or letters:
            if len(letters) >= len(digits):
                final.append(letters.pop())
                if digits:
                    final.append(digits.pop())
            else:
                final.append(digits.pop())
                if letters:
                    final.append(letters.pop())
                
        for i in range(len(final) - 1):
            if final[i].isalpha() == final[i + 1].isalpha() or final[i].isdigit() == final[i + 1].isdigit():
                return ""
        
        return ''.join(final)
        