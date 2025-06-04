class Solution:
    def magicalString(self, n: int) -> int:

        '''
        
        1 2 2 1 1 2 1 2 2

        1 2 2 1 1 2

        '''

        if n <= 3:
            return 1
        
        magic1 = [1, 2, 2]
        magic2 = [1, 2, 2]

        for i in range(n - 3):
            calc = 2 if magic1[-1] == 1 else 1
            if magic2[-1] == 2:
                magic1.append(calc)
                magic1.append(calc)
                magic2.append(magic1[len(magic2)])
            elif magic2[-1] == 1:
                magic1.append(calc)
                magic2.append(magic1[len(magic2)])
            
            #print(magic1, magic2)
        
        '''
        1221121221221121122
        '''

        

        return sum(x for x in magic2 if x == 1)
        
        print(magic1, magic2)
            

        