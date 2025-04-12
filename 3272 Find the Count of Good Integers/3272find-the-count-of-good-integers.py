class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        # skip by k or start with palindromic

        left = n // 2
        mid = n % 2

        total = 0
        res = []

        if n == 1:
            for p in range(1, 10):
                calc = str(p)
                if int(calc) % k == 0:
                    print(calc)
                    hmap = Counter(calc)
                    
                    idk = factorial(n)
                    for key, val in hmap.items():
                        idk /= factorial(val)
                    
                    if '0' in hmap:
                        idk2 = factorial(n - factorial(n - hmap['0']))
                        for key, val in hmap.items():
                            if key != '0':
                                idk2 /= factorial(val)
                        total += idk - idk2
                    else:
                        total += idk 

            return int(total)    
        
        seen = set()
        for i in range(max(1, 10 ** (left - 1)), 10 ** (left)):
            if mid:
                for p in range(0, 10):
                    calc = str(i) + str(p) + str(i)[::-1]
                    if int(calc) % k == 0:
                        if ''.join(sorted(calc)) in seen:
                            continue
                        seen.add(''.join(sorted(calc)))
                        hmap = Counter(calc)
                        
                        idk = factorial(n)
                        for key, val in hmap.items():
                            idk /= factorial(val)
                        
                        idk2 = 0
                        if '0' in hmap:
                            idk2 = factorial(n - 1)
                            hmap['0'] -= 1
                            for key, val in hmap.items():
                                idk2 /= factorial(val)
                            total += idk - idk2
                        else:
                            total += idk  

                        print(calc, idk - idk2)                    
            else:
                calc = str(i) + str(i)[::-1]
                if int(calc) % k == 0:
                    if ''.join(sorted(calc)) in seen:
                        continue
                    seen.add(''.join(sorted(calc)))
                    hmap = Counter(calc)
                    
                    idk = factorial(n)
                    for key, val in hmap.items():
                        idk /= factorial(val)
                    
                    if '0' in hmap:
                        idk2 = factorial(n - 1)
                        hmap['0'] -= 1
                        for key, val in hmap.items():
                            idk2 /= factorial(val)
                        total += idk - idk2
                    else:
                        total += idk   
                 
        
        return int(total)



        