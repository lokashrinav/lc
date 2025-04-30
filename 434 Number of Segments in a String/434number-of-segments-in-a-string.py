class Solution:
    def countSegments(self, s: str) -> int:
        
        idk = s.split(" ")

        if s == "":
            return 0

        length = 0
        for elem in idk:
            if elem:
                length += 1

        return length