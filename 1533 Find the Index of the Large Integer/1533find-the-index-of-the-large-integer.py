# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        '''
        0, 4
        0, 1, 2, 3, 4        
        '''
        while l <= r:
            m = (l + r + 1) // 2
            flag = (r - l) % 2 == 1
            if flag:
                if m - 1 >= l:
                    calc = reader.compareSub(l, m - 1, m, r)
                else:
                    return m
            else:
                calc = reader.compareSub(l, m, m, r)

            print(l, r, m, calc)

            if calc == 0:
                return m
            elif calc == 1:
                r = m - 1
            else:
                if flag:
                    l = m
                else:
                    l = m + 1


        