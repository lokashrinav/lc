class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        hmap = Counter(words)

        total = 0
        flag = False

        for key, val in hmap.items():
            elem = key
            str1 = elem[1] + elem[0]
            if elem[0] == elem[1]:
                if flag:
                    if val % 2:
                        val -= 1
                    total += val
                else:
                    total += val
                    if val % 2:
                        flag = True
            elif str1 in hmap:
                total += min(hmap[str1], hmap[elem])
                
        return int(total) * 2
