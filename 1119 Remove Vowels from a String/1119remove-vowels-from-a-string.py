class Solution:
    def removeVowels(self, s: str) -> str:
        new_str = []

        for char in s:
            if char not in 'aeiou':
                new_str.append(char)
        
        return ''.join(new_str)
        