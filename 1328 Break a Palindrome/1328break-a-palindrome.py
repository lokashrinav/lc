class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""
        else:
            palindrome = list(palindrome)
            flag = False
            length = (len(palindrome)) // 2
            for i in range(length):
                if palindrome[i] != 'a':
                    palindrome[i] = 'a'
                    flag = True
                    break

            if not flag:
                palindrome[-1] = 'b'
            
            return ''.join(palindrome)
                    


        