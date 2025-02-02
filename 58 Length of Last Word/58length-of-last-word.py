class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        idk = s.split()
        return len(idk[-1])