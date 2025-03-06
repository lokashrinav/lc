class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        '''

        1 ^ 433852

        2 ^ 10

        2 ^ 5 

        '''
        '''b = int(''.join(map(str, b)))
        
        def dfs(a, b):
            if a == 1:
                return 1
            if b == 1:
                return a

            times = 1
            if b % 2:
                times = a
            
            calc = dfs(a, b // 2) % 1337

            return (calc * calc * times) % 1337
        
        return dfs(a, b) % 1337'''
        
        '''
        2 ** 100
        '''
        a = a % 1337

        for i in range(len(b)):
            b[i] = str(b[i])

        b = int(''.join(b)) % 1337

        b = str(b).split()

        for i in range(len(b)):
            b[i] = int(b[i])

        if a == 1:
            return 1
        
        final = 1
        curr = a
        for i in range(len(b) - 1, -1, -1):
            final *= curr ** b[i] % 1337
            curr **= 10
        
        return final % 1337