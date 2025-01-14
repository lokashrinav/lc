class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split(' ')

        str1 = ""
        for i in range(len(lis) - 1, -1, -1):
            idk = " "
            if lis[i]:
                str1 += lis[i] + idk
        
        return str1[:-1]
        