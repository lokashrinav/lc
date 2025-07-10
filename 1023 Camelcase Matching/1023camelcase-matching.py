class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        '''

        O(n) * O(a) * O(b)

        100 * 100 * 100

        '''

        def sub(elem1, elem2):
            ind = 0
            flag = False
            for i in range(len(elem2)):
                if not flag and elem2[i] == elem1[ind]:
                    ind += 1
                    if ind == len(elem1):
                        flag = True
                elif elem2[i].upper() == elem2[i]:
                    return False
            
            return flag

        res = []
        for elem in queries:
            res.append(sub(pattern, elem))
        
        return res
        

