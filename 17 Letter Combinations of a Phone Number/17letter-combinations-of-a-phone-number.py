class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        curr = []
        hmap = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        def back(i):
            if i >= len(digits):
                res.append(''.join(curr))
                return
            for p in hmap[digits[i]]:
                curr.append(p)
                back(i + 1)
                curr.pop()

        back(0)
        return res
        