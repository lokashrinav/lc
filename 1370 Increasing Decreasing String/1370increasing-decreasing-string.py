class Solution:
    def sortString(self, s: str) -> str:


        arr = [0] * 26
        for elem in s:
            arr[ord(elem) - 97] += 1

        def is_zero(arr):
            for elem in arr:
                if elem != 0:
                    return True
            
            return False

        str1 = ""
        while is_zero(arr):
            for i in range(len(arr)):
                if arr[i] > 0:
                    str1 += chr(i + 97)
                    arr[i] -= 1
            
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] > 0:
                    str1 += chr(i + 97)
                    arr[i] -= 1

            print(arr)

        return str1


        