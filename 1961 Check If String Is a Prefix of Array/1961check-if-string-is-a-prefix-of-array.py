class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        

        l, r = 0, len(words) - 1
        saved = False

        while l <= r:
            m = (l + r) // 2
            str1 = ""
            for i in range(m+1):
                str1 += words[i]
            
            print(str1)
            if str1 == s:
                return True
            elif len(str1) > len(s):
                r = m - 1
            else:
                l = m + 1

        return saved