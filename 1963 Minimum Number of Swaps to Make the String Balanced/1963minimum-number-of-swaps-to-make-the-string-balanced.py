class Solution:
    def minSwaps(self, s: str) -> int:

        '''

        -1

        1

        ][][[]

        [[]][]

        [][][[[[]]]]

        ]][]][[[]]]]

        '''

        s = list(s)
        left = right = 0
        count = 0
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and left >= 0:
                if s[l] == "[":
                    left += 1
                else:
                    left -= 1
                if left < 0:
                    break
                l += 1

            while l < r and right >= 0:
                if s[r] == "]":
                    right += 1
                else:
                    right -= 1

                if right < 0:
                    break
                r -= 1

            
            if l < r:
                s[l], s[r] = s[r], s[l]    
                count += 1
                l += 1
                r -= 1
                left += 2
                right += 2
            
            '''
            ]]][[[

            []][[]
            '''

        #print(s)

        return count
                    
                





        