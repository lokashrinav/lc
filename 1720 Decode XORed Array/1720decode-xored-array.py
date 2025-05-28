class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        '''

        2, 3

        1, 0, 2, 1

        '''

        curr = [first]

        for i in range(len(encoded)):
            curr.append(encoded[i] ^ curr[-1])
        
        return curr
