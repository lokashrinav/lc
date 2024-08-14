class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def LDS(needle):
            arr = [0] * len(needle)
            i = 1
            length = 0
            while i < len(needle):
                if needle[i] == needle[length]:
                    length += 1
                    arr[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = arr[length - 1]
                    else:
                        arr[i] = 0
                        i += 1
            return arr
        
        arr = LDS(needle)
        j = 0
        ind = -1

        for i in range(len(haystack)):
            while (j > 0 and haystack[i] != needle[j]):
                j = arr[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == len(needle):
                ind = i - len(needle) + 1
                break
                j = arr[j - 1]

        return ind
        
        


        