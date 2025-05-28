class Solution:
    def repeatedCharacter(self, s: str) -> str:

        hset = set()

        for elem in s:
            if elem in hset:
                return elem
            hset.add(elem)
        