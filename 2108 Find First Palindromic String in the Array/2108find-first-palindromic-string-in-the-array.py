class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for elem in words:
            if elem == elem[::-1]:
                return elem
        
        return ''