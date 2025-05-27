class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        arr = [-1] * len(bits)
        while i < len(bits):
            if bits[i] == 1:
                arr[i] = arr[i + 1] = 1
                i += 1
            else:
                arr[i] = 0
            i += 1
        
        return True if arr[-1] == 0 else False

        

        

        