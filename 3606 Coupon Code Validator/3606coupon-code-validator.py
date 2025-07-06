class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        def coup(first):
            for i in range(len(first)):
                if first[i].isalnum() or first[i] == "_":
                    continue
                return False
                
            return True

        res = []
        arr = ["electronics", "grocery", "pharmacy", "restaurant"]

        hmap = {}
        for i in range(len(arr)):
            hmap[arr[i]] = i

        for i in range(len(code)):
            if code[i] and coup(code[i]) and businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and isActive[i]:
                res.append((businessLine[i], code[i]))
                

        def func(a, b):
            if hmap[a[0]] > hmap[b[0]]:
                return 1
            elif hmap[a[0]] < hmap[b[0]]:
                return -1
            else:
                return 1 if a[1] > b[1] else -1
            
        res.sort(key=cmp_to_key(func))
        
        return [elem[1] for elem in res]
        