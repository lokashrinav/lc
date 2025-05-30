class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        

        ind = bisect_left(letters, chr(ord(target) + 1))

        if ind == len(letters):
            return letters[0]

        return letters[ind]