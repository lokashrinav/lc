class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        '''

        ah


        
        '''
        
        char_map = Counter(chars)

        total = 0

        for word in words:
            hmap = Counter(word)
            flag = True

            for key, val in hmap.items():
                if val > char_map[key]:
                    flag = False
            
            #print(hmap, char_map)
            
            if flag:
                total += len(word)
        
        return total

                

        