class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''
        
        Trie

        '''

        '''class Node:
            def __init__(self, val):
                self.curr = val
                self.isend = False
                self.hmap = {}

        for i in range(len(products)):'''

        products.sort()

        curr = ""
        final = []
        for i in range(len(searchWord)):
            res = []
            curr += searchWord[i]
            ind = bisect_left(products, curr)
            for p in range(ind, min(ind + 3, len(products))):
                first = products[p]
                if curr == first[:len(curr)]:
                    res.append(first)
            final.append(res)
        
        return final


